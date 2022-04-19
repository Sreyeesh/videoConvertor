import json
import sys
from pathlib import Path
import ffmpeg

import compression
from src.Gui import VideoConvertor
from src.ParseArgs import ParseArgs
from src.DirsSettings import DirsSettings

if __name__ == "__main__":
    dirs = DirsSettings("settings.json")
    settings = dirs.get_settings()
    names = [x.get("name") for x in settings]
    p = ParseArgs(names, str(Path(__file__).parts[-1]))
    args = p.parse_args()
    if not args.nogui:
        root_window = VideoConvertor()
        root_window.mainloop()
        sys.exit()
    if args.run_all:
        compression.reduce_dem_all()
    elif args.delete_setup:
        dirs.delete_setup(args.name)
    else:
        entry = {
            "in_dir": args.in_dir,
            "out_dir": args.out_dir,
            "out_ftype": args.out_ftype,  # Always mp4
            "audio_brate": args.audio_brate,
            "video_brate": args.video_brate,
            "video_res": args.video_res,
            "add_ext": args.add_ext,
            "name": args.name
        }
        dirs.save_new_entry(entry)
