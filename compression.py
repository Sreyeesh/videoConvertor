from moviepy.editor import *
from src.DirMapper import DirMapper
from src.DirsSettings import DirsSettings


def reduce_dem_all():
    d_mapper = DirMapper(DirsSettings('settings.json').get_settings())
    for inf, of, settings in d_mapper.get_dir_mappings():
        # Calculate resize factor from Y-axis.
        reduce_size(str(inf), str(of), settings)


def reduce_size(file_in, file_out, settings):
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