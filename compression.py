from pathlib import Path

from moviepy.editor import *
from src.DirMapper import DirMapper
from src.DirsSettings import DirsSettings


def reduce_dem_all(logger = None):
    settings = DirsSettings('settings.json').get_settings()
    d_map = DirMapper(settings)
    # Filter only those jobs for which target doesn't exist.
    d_map = [x for x in d_map.get_dir_mappings() if not x[1].exists()]
    for inf, of, settings in d_map:
        # Calculate resize factor from Y-axis.
        recode(str(inf), str(of), settings)


def recode(in_file: str, out_file: str, settings, logger=None):
    x, y = [int(a) for a in settings["output_video_resolution"].split("x")]
    with VideoFileClip(in_file, target_resolution=(y, x)) as clip:
        clip.write_videofile(out_file,
                             fps=None,  # TODO: configurable out-file fps
                             audio_codec="libmp3lame",
                             audio_bitrate=str(settings["audio_bitrate_kbps"]) + "K",
                             preset="placebo",
                             threads=4,  # TODO: Configurable threads.
                             logger=logger)


def reduce_size(file_in, file_out, settings, logger):
    resolution = settings["video_res"]
    video_inputs = VideoFileClip(file_in)
    # Calculate resize-factor from Y-axis.
    resize_factor = resolution[1] / video_inputs.h
    video_outputs = video_inputs.resize(resize_factor)
    # TODO: Add setting for fps
    print(file_out)
    video_outputs.write_videofile(str(file_out),
                                  fps=30,
                                  codec="libx264",
                                  bitrate=str(settings.get("video_brate")) + "K",
                                  audio_bitrate=str(settings.get("audio_brate")) + "K",
                                  preset="placebo")

    width = video_inputs.w
    height = video_inputs.h

    print("size of video is : ", end='')
    print(str(width) + "x", str(height))

    width_2 = video_outputs.w
    height_2 = video_outputs.h

    print("This is the size of the new video: ", end=" ")
    print(str(width_2) + "x", str(height_2))
    print(str(width_2) + "x", str(height_2))
