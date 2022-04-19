import json
import sys
from pathlib import Path
import ffmpeg

import compression
from src.Gui import VideoConvertor
from src.ParseArgs import ParseArgs
from src.DirsSettings import DirsSettings

if __name__ == "__main__":
    root_window = VideoConvertor()
    root_window.mainloop()
