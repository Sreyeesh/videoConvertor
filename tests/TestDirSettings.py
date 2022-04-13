import os
import unittest
from pathlib import Path

from Auxialiry import get_temp_files_dir
from src.DirsSettings import DirsSettings


class TestDirSettings(unittest.TestCase):

    def setUp(self) -> None:
        tmp_dir = get_temp_files_dir()
        os.chdir(tmp_dir)

        cwd = Path(".")
        self.in_dir = cwd / Path("in_dir")
        self.out_dir = cwd / Path("out_dir")
        self.in_dir.mkdir()
        self.out_dir.mkdir()
        self.dir_settings = DirsSettings("test.json")
        self.entry = {
            "in_dir": self.in_dir,
            "out_dir": self.out_dir,
            "out_ftype": "mp4",
            "audio_brate": 256,
            "video_brate": 400,
            "video_res": [1024, 768],
            "add_ext": "_postfix",
            "name": "Somename"
        }


    def tearDown(self) -> None:
        self.in_dir.rmdir()
        self.out_dir.rmdir()
        Path("./test.json").unlink()

    def test_relative_paths(self):
        # Test inputting relative paths to DirSettings.
        self.dir_settings.save_new_entry(self.entry)
        settings = self.dir_settings.get_settings()

        self.assertTrue(Path(settings[0]["in_dir"]).is_absolute(),
                        f"Path in settings is not converted to absolute: {settings[0]['in_dir']}")
