from moviepy.editor import *


def recode(in_file: str, out_file: str, settings, logger=None):
    orig = True
    if "Original" not in settings["output_video_resolution"]:
        x, y = [int(a) for a in settings["output_video_resolution"].split("x")]
    with VideoFileClip(in_file, target_resolution=(y, x) if not orig else None) as clip:
        print(settings["output_fps"])
        clip.write_videofile(out_file,
                             fps=int(settings["output_fps"]),
                             audio_codec="libvorbis",
                             audio_bitrate=str(settings["audio_bitrate_kbps"]) + "K",
                             preset="placebo",
                             threads=8,
                             logger=logger)
