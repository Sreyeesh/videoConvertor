from moviepy.editor import *


def recode(in_file: str, out_file: str, settings, logger=None):
    x, y = [int(a) for a in settings["output_video_resolution"].split("x")]
    with VideoFileClip(in_file, target_resolution=(y, x)) as clip:
        print(settings["output_fps"])
        clip.write_videofile(out_file,
                             fps=int(settings["output_fps"]),  # TODO: configurable out-file fps
                             audio_codec="libmp3lame",
                             audio_bitrate=str(settings["audio_bitrate_kbps"]) + "K",
                             preset="placebo",
                             threads=4,  # TODO: Configurable threads.
                             logger=logger)


# def reduce_size(file_in, file_out, settings, logger):
#     resolution = settings["video_res"]
#     video_inputs = VideoFileClip(file_in)
#     # Calculate resize-factor from Y-axis.
#     resize_factor = resolution[1] / video_inputs.h
#     video_outputs = video_inputs.resize(resize_factor)
#     # TODO: Add setting for fps
#     print(file_out)
#     video_outputs.write_videofile(str(file_out),
#                                   fps=30,
#                                   codec="libx264",
#                                   bitrate=str(settings.get("video_brate")) + "K",
#                                   audio_bitrate=str(settings.get("audio_brate")) + "K",
#                                   preset="placebo")
#
#     width = video_inputs.w
#     height = video_inputs.h
#
#     print("size of video is : ", end='')
#     print(str(width) + "x", str(height))
#
#     width_2 = video_outputs.w
#     height_2 = video_outputs.h
#
#     print("This is the size of the new video: ", end=" ")
#     print(str(width_2) + "x", str(height_2))
#     print(str(width_2) + "x", str(height_2))
