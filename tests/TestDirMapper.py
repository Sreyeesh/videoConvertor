import unittest
import os
from pathlib import Path

from src.DirMapper import DirMapper
from tests.Auxialiry import get_temp_files_dir


class TestDirMapper(unittest.TestCase):

    def setUp(self) -> None:
        # Create temp dirs for input and output, and make some files.
        temp_path = get_temp_files_dir()
        self.in_dir = temp_path / Path("in_dir")
        self.in_dir.mkdir()
        self.video1 = self.in_dir / Path("video1.avi")
        self.video2 = self.in_dir / Path("video2.avi")
        self.video1.touch()
        self.video2.touch()

        self.out_dir = temp_path / Path("out_dir")
        self.out_dir.mkdir()

        self.settings = [
            {
                "in_dir": str(self.in_dir),
                "out_dir": str(self.out_dir),
                "out_ftype": "mp4",
                "audio_brate": 128,
                "video_brate": 400,
                "video_res": [
                    1024,
                    768
                ],
                # TODO: Change add_ext to add_postfix to not confuse it to file extension.
                "add_ext": "_youtube",
                "name": "TestSetup"
            },
            {
                "in_dir": str(self.in_dir),
                "out_dir": str(self.out_dir),
                "out_ftype": "mp4",
                "audio_brate": 128,
                "video_brate": 400,
                "video_res": [
                    1024,
                    768
                ],
                "add_ext": "_discord",
                "name": "TestSetup2"
            }
        ]
        self.dir_mapper = DirMapper(self.settings)

    def tearDown(self) -> None:
        self.video1.unlink()
        self.video2.unlink()
        self.in_dir.rmdir()
        for f in os.scandir(self.out_dir):
            f: Path
            if f.is_file() and f.exists():
                f.unlink()
        self.out_dir.rmdir()

    def test_get_dir_mappings(self):
        mappings = self.dir_mapper.get_dir_mappings()
        self.assertEqual(len(mappings), 4)
        self.assertEqual(len(mappings[0]), 3)
