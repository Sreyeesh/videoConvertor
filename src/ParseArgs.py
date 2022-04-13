import argparse
from enum import Enum
from pathlib import Path


class Actions(Enum):
    manage_dirs = 1
    manage_enc_profiles = 2
    manage_enc_profile_settings = 3


class ParseArgs(argparse.ArgumentParser):

    def __init__(self, names=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names = names
        self.populate_options()

    def populate_options(self):
        name = self.add_argument("--name", type=str,
                                 help=f"All configs should have a name. [{', '.join(self.names)}]",
                                 required=True)
        dirs = self.add_argument_group("DIRS")
        dirs.add_argument("--delete-setup", action="store_true", default=False)
        dirs.add_argument("--in-dir", type=str)
        dirs.add_argument("--out-dir", type=str)
        dirs.add_argument("--add-ext", type=str, help="File naming postfix for output.")

        enc = self.add_argument_group("ENC")
        enc.add_argument("--out-ftype", type=str, choices=("webm", "mp4"),
                         help="Output filetype.")
        enc.add_argument("--audio-brate", type=int, help="Audio bitrate kbps.")
        enc.add_argument("--video-brate", type=int, help="Video bitrate kbps.")
        enc.add_argument("--video-res", type=int, nargs=2, help="X Y resolution")

