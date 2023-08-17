# The function of this program is to visualize depth and rgb images side by side

import os
import cv2

# rgb and depth image directories
rgb_path = "/home/mahderekaltaye/Documents/trial2/aligned_stitch/new_code_oldsensor/rgb"
depth_path = "/home/mahderekaltaye/Documents/trial2/aligned_stitch/new_code_oldsensor/depth"

# loop through all the files in the folder and sort
rgb_files = sorted([f for f in os.listdir(rgb_path) if not f.startswith('.')])
depth_files = sorted([f for f in os.listdir(depth_path) if not f.startswith('.')])

# resizing dimensions 
width = 640
height = 480

# empty list to add array of depth and rgb concatenated images
concat_images = [] 

# specifying output dimensions 
output_width = 640
output_height = 480
fps = 30.0 # frame per second for video conversion

# read images in both depth and rgb folders, resize to same 
# dimensions and concatinate the images
for rgb_file, depth_file in zip(rgb_files, depth_files):
    rgb_dir = os.path.join(rgb_path, rgb_file)
    depth_dir = os.path.join(depth_path, depth_file)

    # read the images    
    rgb_image = cv2.imread(rgb_dir)
    depth_image = cv2.imread(depth_dir)

    # make sure both images have the same width and height
    rgb_image = cv2.resize(rgb_image, (width, height))
    depth_image = cv2.resize(depth_image, (width, height))

    # convert depth image to 3-channel format if it has an alpha channel
    if depth_image.shape[2] == 4:
        depth_image = cv2.cvtColor(depth_image, cv2.COLOR_BGRA2BGR)
    
    # concatinate images or view rgb data adjacent to depth
    concatinated_images = cv2.hconcat([rgb_image, depth_image])
    concat_images.append(concatinated_images)
    
# create an output_video object to save the concatinated images as a video
# replace video output path and name
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter("/home/mahderekaltaye/Documents/trial2/aligned_stitch/new2.mp4", fourcc, fps, (2 * width, height))

# write each merged image to the video file
for image in concat_images:
    output_video.write(image)

# release the video writer
output_video.release()

## Troubleshooting
## uncomment the following code to display the adjacent images saved to the concatinated_images array 
#from PIL import Image
#from IPython.display import display

## open the adjacent image using PIL's Image module
## replace 160 with any number to see different sequences 
#merged_image = Image.fromarray(concat_images[160])

## display the image 
#display(merged_image)