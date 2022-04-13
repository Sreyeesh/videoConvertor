from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

original_path = os.path.join(SAMPLE_INPUTS, '/Users/sreyeeshgarimella/Documents/videoConvertor/videoConvertor/data/samples/inputs/sample.mp4')
thumbnail_directory = os.path.join(SAMPLE_OUTPUTS, "/Users/sreyeeshgarimella/Documents/videoConvertor/videoConvertor/data/samples/thumbnails")
print(original_path)

clip = VideoFileClip(original_path)
print("frames in seconds",clip.reader.fps) # frames per second
print("number of frames",clip.reader.nframes)
print("duration",clip.duration) # seconds 

frame_duration = clip.duration
max_duration = int(frame_duration) + 1
for i in range(0,max_duration):
    for i in range(0, max_duration):
        frame_duration = clip.get_frame(i)
    # print(frame) # np.array numpy array # inference
    new_img_filepath = os.path.join(thumbnail_directory, f"{i}.jpg")
    # print(f"frame at {i} seconds saved at {new_img_filepath}")
    new_img = Image.fromarray(frame_duration)
    new_img.save(new_img_filepath)
    