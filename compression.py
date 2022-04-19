from moviepy.editor import *
from src.DirMapper import DirMapper
from src.DirsSettings import DirsSettings


def reduce_dem_all():
    d_mapper = DirMapper(DirsSettings('settings.json').get_settings())
    for inf, of, settings in d_mapper.get_dir_mappings():
        # Calculate resize factor from Y-axis.
        reduce_size(inf, of, settings.get("video_res"))


def reduce_size(file_in, file_out, resolution):

    video_inputs = VideoFileClip(str(file_in))
    # Calculate resize-factor from Y-axis.
    resize_factor = video_inputs.h / resolution[1]
    video_outputs = video_inputs.resize(resize_factor)

    width = video_inputs.w
    height = video_inputs.h

    print("size of video is : ", end='')
    print(str(width) + "x", str(height))

    width_2 = video_outputs.w
    height_2 = video_outputs.h

    print("This is the size of the new video: ", end=" ")
    print(str(width_2) + "x", str(height_2))

    # video_outputs.ipython_display(width=480)


reduce_dem_all()
