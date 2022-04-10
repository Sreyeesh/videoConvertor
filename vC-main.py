
"""
 compressing video formats and convertion for different platforms
     
"""

import os
from pathlib import Path
import sys
import ffmpeg

def compress_video(video_full_path, size_upper_bound, two_pass=True, filename_suffix='1'):
   
    filename, extension = Path.splitext(video_full_path)
    extension = '.mp4'
    output_file_name = filename + filename_suffix + extension

    total_bitrate_lower_bound = 11000
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000
    min_video_bitrate = 100000