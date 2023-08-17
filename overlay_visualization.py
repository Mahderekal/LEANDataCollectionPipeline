# The main function of this code is to visualize depth data overlayed on rgb data 

import os
import cv2


# rgb and depth image directories
rgb_path = "/home/mahderekaltaye/Documents/trial2/2b_NW_lighton/rgb"
depth_path = "/home/mahderekaltaye/Documents/trial2/2b_NW_lighton/depth"

# resizing dimensions
height = 480
width = 640
fps = 20  

# empty list to add array of depth and rgb blended images
blended_imgs = [] 

# loop through all image files in each folder and sort
rgb_image_list = sorted([f for f in os.listdir(rgb_path) if f.endswith((".png",".jpeg",".jpg"))])
depth_image_list = sorted([f for f in os.listdir(depth_path) if f.endswith((".png",".jpeg",".jpg"))])

# loop through images in the paths, resize, overlay one ontop of the other, and save it in 
# the empty list created (blended_imgs) 
for rgb_image, depth_image in zip(rgb_image_list, depth_image_list):
    rgbim = cv2.imread(os.path.join(rgb_path, rgb_image))  # joining images with their paths
    depthim = cv2.imread(os.path.join(depth_path, depth_image))
    
    resized_rgbim = cv2.resize(rgbim, (width, height)) # resizing images
    resized_depthim = cv2.resize(depthim, (width, height))
    
    overlay = cv2.addWeighted(resized_rgbim, 0.7, resized_depthim, 0.6, 0) # overlaying 
    blended_imgs.append(overlay) # save blended or overlayed images to empty array

# create a output_video object to save the blended images as a video
# replace video output path and name    
fourcc = cv2.VideoWriter_fourcc(*'mp4v')   
output_video = cv2.VideoWriter("/home/mahderekaltaye/Documents/trial2/Videos/2b_NW_lighton.mp4",fourcc, fps, (width, height))

# write each blended image to the video file
for image in blended_imgs:
    output_video.write(image)

# release the video writer
output_video.release()


## Troubleshooting
## uncomment the following code to display the adjacent images saved to the concatinated_images array 
#from PIL import Image
#from IPython.display import display

## open the blended image using PIL's Image module
## replace 160 with any number to see different sequences 
#blended_image = Image.fromarray(blended_imgs[160])

# display the image
#display(blended_image)
