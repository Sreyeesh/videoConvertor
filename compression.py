from moviepy.editor import *
from src.DirMapper import DirMapper
from src.DirsSettings import DirsSettings


# TODO: reduce_dem_all and reduce_size should be written to accommodate the following options.
# [  # EXAMPLE. Something like this is what you get from gui, when user clicks `Run all`.
#   {
#     "in_dir": "C:/Users/mkuja/source/repos/videoConvertor/data/samples/inputs",
#     "out_dir": "C:/Users/mkuja/source/repos/videoConvertor/data/samples/output",
#     "out_ftype": "mp4",
#     "audio_bitrate_kbps": 128,
#     "video_bitrate_mbps": 0.8,
#     "output_file_postfix": "_example",
#     "name": "My SomeProfile"
#   }
# ]


def reduce_dem_all(settings=None):
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
    print(str(width_2) + "x", str(height_2))
