import platform
import random
import unittest
import os
import string
from hashlib import sha256
from itertools import permutations
from pathlib import Path
from tempfile import TemporaryFile

from sqlalchemy import create_engine, select

from src.Models.Files import Base
from src.Services.FilesService.FilesService import FilesService


# TODO: Only needed by TestFilesService. If needed elsewhere, consider making it a service.
def get_temp_file_path():
    if "Windows" in platform.system():
        while True:
            fname = "".join(random.choices(string.ascii_lowercase, k=8))
            full_path = Path(f"{os.path.expanduser('~')}\\AppData\\Local\\Temp\\{fname}")
            if full_path.exists():
                continue
            return full_path
    else:
        while True:
            fname = "".join(random.choices(string.ascii_lowercase, k=8))
            full_path = Path(f"/tmp/{fname}")
            if full_path.exists():
                continue
            return full_path


class TestFilesService(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)

        self.files_service = FilesService(self.engine)

        # Test file path.
        self.tmp_file_path = get_temp_file_path()
        with open(self.tmp_file_path, "w") as fh:
            fh.write("FUBAR")

        # Test file path 2.
        self.tmp_file_path2 = get_temp_file_path()
        with open(self.tmp_file_path2, "w") as fh:
            fh.write("FUBAR2")

        # create entry in DB for path 2
        stmt = self.files_service.create_file_entry(file_path=self.tmp_file_path2)

    def tearDown(self) -> None:
        self.tmp_file_path.unlink()
        self.tmp_file_path2.unlink()

    def test_get_by_absolute_path_works(self):
        path = self.files_service.get_by_absolute_path(self.tmp_file_path2)
        self.assertEqual(path.absolute_path, str(self.tmp_file_path2))

    def test_update_file_entry_works(self):
        with open(self.tmp_file_path2, "w") as fh:
            fh.write("BAFUR!")

        m = sha256()
        m.update(self.tmp_file_path2.read_bytes())
        hash_ = m.hexdigest()

        self.assertNotEqual(hash_, self.files_service.get_by_absolute_path(
            self.tmp_file_path2).hash)
        self.files_service.update_file_entry(self.tmp_file_path2)
        self.assertEqual(hash_, self.files_service.get_by_absolute_path(self.tmp_file_path2).hash)
