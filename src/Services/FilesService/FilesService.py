from hashlib import sha256
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from ..BaseService import BaseService
from ..Exeptions import InvalidPath
from ...Models.Files import File


class FilesService(BaseService):

    def __init__(self, sql_alchemy_engine: Engine):
        super().__init__()
        self.engine = sql_alchemy_engine

    def _path_checks(self, path: Path):
        if not path.is_file():
            raise InvalidPath("file_path doesn't point to a file.")
        if not path.is_absolute():
            raise InvalidPath("file_path isn't absolute.")

    def _hash(self, path: Path):
        # Calculate hash
        m = sha256()
        with open(path, "rb") as fh:
            while content := fh.read(1024 ** 2):
                m.update(content)
        hash_ = m.hexdigest()
        return hash_

    def update_file_entry(self, file_path: Path):
        self._path_checks(file_path)

        stats = file_path.stat()
        with Session(self.engine) as session:
            stmt = select(File).where(File.absolute_path == str(file_path))
            file = session.scalar(stmt)
            if not file:
                raise InvalidPath("No such file_path in database. Use create_file instead.")
            file.c_time = stats.st_ctime
            file.m_time = stats.st_mtime
            session.add(file)
            session.commit()

    def create_file_entry(self, file_path: Path):
        self._path_checks(file_path)
        stats = file_path.stat()

        #hash_ = self._hash(file_path)
        with Session(self.engine) as session:
            db_entry = File(
                absolute_path=str(file_path),
                c_time=stats.st_ctime,
                m_time=stats.st_mtime
            )
            session.add(db_entry)
            session.commit()

    def get_by_absolute_path(self, path: Path):
        with Session(self.engine) as session:
            stmt = select(File).where(File.absolute_path == str(path))
            return session.scalar(stmt)

    def has_changed(self, path: Path):
        with Session(self.engine) as session:
            stmt = select(File).where(File.absolute_path == str(path))
            from_db = session.scalar(stmt)
            abs_path = from_db.absolute_path == str(path)
            ctime = from_db.c_time == path.stat().st_ctime
            mtime = from_db.m_time == path.stat().st_mtime
            return abs_path == ctime == mtime == True

