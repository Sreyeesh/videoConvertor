from abc import ABC
from datetime import datetime
from hashlib import sha256
from os.path import getatime, getctime
from pathlib import Path


class BaseFileWatcher(ABC):

    def __init__(self, file_path: Path):
        pass

    def has_changed(self) -> bool:
        pass

    def ctime(self) -> datetime:
        pass

    def ctime_in_db(self):
        pass

    def atime(self) -> datetime:
        pass

    def mtime_in_db(self):
        pass

    def hash(self) -> str:
        pass

    def md5_in_db(self):
        pass


class FileWatcher(BaseFileWatcher):
    """Can be polled for file changes."""

    def __init__(self, file_path: Path):
        self.path = file_path

    def has_changed(self) -> bool:
        pass  # TODO: Needs  file_DB service

    def ctime(self) -> datetime:
        getctime()

    def ctime_in_db(self):
        super().ctime_in_db()

    def mtime_in_db(self):
        super().atime_in_db()

    def hash_in_db(self):
        super().md5_in_db()

    def mtime(self) -> datetime:
        getatime(self.path)

    def hash(self) -> str:
        with open(self.path, "rb") as fh:
            sha = sha256()
            while fh:
                sha.update(bytes(fh.read(1024**2)))
            return sha.hexdigest()
