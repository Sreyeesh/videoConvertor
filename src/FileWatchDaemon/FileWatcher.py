import os
from os import _ScandirIterator
from pathlib import Path
from typing import List

from src.Services.Exeptions import ArgumentError, InvalidPath


class FileWatcher:
    def __init__(self, source_path: Path, target_path: Path, suffix:str):
        """Polls that files in source_path have their counterparts in target_path.

        @:argument source_path: Absolute Path.
        @:argument target_path: Absolute Path.
        @:argument suffix: Suffix added to file name from source_path when encoding happens.
        """
        if (not target_path.is_absolute()
                and not source_path.is_absolute()):
            raise InvalidPath("Both source- and target_path must be absolute.")
        self.target_path = target_path
        self.source_path = source_path
        self.suffix = suffix

    def get_missing(self, path):
        """Gets a list of files that miss their counterpart at target_path."""
        ret = []
        for f in os.scandir(path):
            f: Path  # Relative
            if f.is_dir():
                continue
            # If f is a file, and if the counterpart exists in the target_path
            elif (f.is_file()
                  and not (self.target_path / Path(f"{f.parts[-1]}{self.suffix}")).is_file()):
                ret.append((f, self.target_path / Path(f"{f.parts[-1]}{self.suffix}")))
        return ret

    def create_target_dir(self):
        self.target_path.mkdir(mode=0o640, exist_ok=True, parents=True)
