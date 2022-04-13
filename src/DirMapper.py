import os
from pathlib import Path
from typing import List, Dict, Tuple


class InvalidPath(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidPath, self).__init__(*args, **kwargs)


class DirMapper:

    """DirMapper

    Gets all encoding settings for each file in input dirs, their respective output dir and
    encoding settings. Class has only one public method, get_dir_mappings(). See that.
    """

    def __init__(self, dir_settings: List[Dict]):
        self.dir_settings = dir_settings

    def get_dir_mappings(self) -> List[Tuple[Path, Path, Dict]]:
        """Return a list of three-tuples.

        :return Tuple[Path, Path, Dict]
                Where first Path is source path as an absolute Path.
                Second Path is destination path as an absolute Path.
                Dict that contains encoding settings.
        """
        ret = []
        for in_dir, out_dir, enc_settings in (zip([x["in_dir"] for x in self.dir_settings],
                                                  [x["out_dir"] for x in self.dir_settings],
                                                  self.dir_settings)):
            if not Path(in_dir).is_absolute() or not Path(out_dir).is_absolute():
                raise InvalidPath("Either in_dir or out_dir is not absolute.")
            for file in os.scandir(in_dir):
                file: Path
                if file.is_file():
                    fname = Path(file).parts[-1]
                    new_fname = (".".join(fname.split(".")[:-1])
                                 + enc_settings.get("add_ext", enc_settings["name"].lower())
                                 + "." + enc_settings["out_ftype"])
                    ret.append((
                        Path(in_dir) / Path(fname),
                        Path(out_dir) / Path(new_fname),
                        enc_settings
                    ))
        return ret
