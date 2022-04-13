import os
import platform
from pathlib import Path


def get_temp_files_dir() -> Path:
    if "Windows" in platform.system():
        full_path = Path(os.path.expanduser("~\\AppData\\Local\\Temp"))
        return full_path
    else:
        full_path = Path("/tmp/")
        return full_path
