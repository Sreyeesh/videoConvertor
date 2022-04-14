from importlib.resources import path
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from src.DirMapper import DirMapper
from src.DirsSettings import DirsSettings

# original_path = os.path.join(SAMPLE_INPUTS, '/Users/sreyeeshgarimella/Documents/videoConvertor/videoConvertor/data/samples/inputs/DJI_0513.MP4')
# thumbnail_directory = os.path.join(SAMPLE_OUTPUTS, "/Users/sreyeeshgarimella/Documents/videoConvertor/videoConvertor/data/samples/thumbnails")
# clip = VideoFileClip(original_path)

def path_for_file():
   d_mapper = DirMapper(DirsSettings('settings.json').get_settings())
    # print("frames in seconds",clip.reader.fps) # frames per second
    # print("number of frames",clip.reader.nframes)
    # print("duration",clip.duration) # seconds 
    
    
def thumbnail_generation():
    frame_duration = clip.duration
    max_duration = int(frame_duration) + 1
    for i in range(0, max_duration):
        frame_duration = clip.get_frame(i)
    new_img_filepath = os.path.join(thumbnail_directory, f"{i}.jpg")
    new_img = Image.fromarray(frame_duration)
    new_img.save(new_img_filepath)

path_for_file()
thumbnail_generation()