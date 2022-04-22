from moviepy.editor import *


def recode(in_file: str, out_file: str, settings, logger=None):
    x, y = [int(a) for a in settings["output_video_resolution"].split("x")]
    with VideoFileClip(in_file, target_resolution=(y, x)) as clip:
        print(settings["output_fps"])
        clip.write_videofile(out_file,
                             fps=int(settings["output_fps"]),
                             audio_codec="libmp3lame",
                             audio_bitrate=str(settings["audio_bitrate_kbps"]) + "K",
                             preset="placebo",
                             threads=8,
                             logger=logger)
