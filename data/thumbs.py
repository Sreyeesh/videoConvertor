from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
original_path = os.path.join(SAMPLE_INPUTS, '/Users/sreyeeshgarimella/Documents/videoConvertor/videoConvertor/data/samples/inputs/sample.mp4')
thumbnail_directory = os.path.join(SAMPLE_OUTPUTS, "/Users/sreyeeshgarimella/Documents/videoConvertor/videoConvertor/data/samples/thumbnails")
os.makedirs(thumbnail_directory)
print(original_path)

clip = VideoFileClip(original_path)
print("frames in seconds",clip.reader.fps) # frames per second
print("number of frames",clip.reader.nframes)
print("duration",clip.duration) # seconds 

frame_duration = clip.duration
max_duration = int(frame_duration) + 1
for i in range(0,max_duration):
    print(f"frame at {i} seconds")
    frames = clip.get_frame(i)
    print(frames) 
    new_image = Image.fromarray(frames)
    new_image.save()