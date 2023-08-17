Instructions for Data Collection Pipeline
============

An end-to-end instruction on data collection using Intel RealSense Depth Camera D435i, running uncertainty estimation algorithm using aquired data, and data visualization.

Lab website: [lean.mit.edu](https://lean.mit.edu/)
## Introduction
Traditionally depth estimation is done using depth sensors such as Intel’s D435i, which are large, heavy and energy intensive. Low energy robots on the other hand have limited energy and load-carrying capacity. Therefore, researchers are now using Deep Neural Networks for depth estimation. Even so, it’s hypothesized that models with better generalization capabilities are more energy intensive and require data to be ready prior to training. This is not only limiting for low-energy robots but also limits robot performance in real-world scenarios where data is available sequentially. As a solution, in the LEAN lab, we use  small DNN models to train small robots online on-the-fly. To build more reliable depth estimation DNNs, we use aleatoric (data inherent) and epistemic (model inherent) uncertainty estimation techniques. 

To conduct this research, we collected datasets in interesting and challenging conditions including optical illusion and environment brightness changes. We then run aleatoric and epistemic (ensamble) uncertainty methods from Uncertainty from Motion algorithm [[1]](#1) on these datasets to qualitatively and quantitatively analyze how both methods perform. This repo contains an end-to-end instruction guide on how to conduct data collection and visualization process as well as running uncertainty estimation methods using Uncertainty from Motion algorithm. Additionally, it contians adjacent and overlay depth and RGB data visulization programs. 

## Get Started
Instructions for the data collection process on a Windows OS are listed in the first section. These are steps taken to collect RGB and depth data from Intel RealSense D435i depth sensor on a Windows OS.

**Note:** Currently, PyRealSense does not have a distribution that’s compatible with the new M1 chip Macbook laptops due to it’s ARM based architecture. Therefore, if you have an M1 chip macbook, I recommend that you conduct at least the data collection process on a windows machine (windows dualboot with a linux OS should be fine). In addition, the Realsense library installation is not supported on a Virtual Machine due to the USB 3.0 translation layer between native hardware and virtual machine, see (https://dev.intelrealsense.com/docs/compiling-librealsense-for-linux-ubuntu-guide) for more details.

Instructions on running uncertainty estimation algorithms on collected data is outlined in second section followed by data visualization instructions in the third section (both using a Linux OS). 

## 1. Data Collection
**System Requirements:** Windows 10 and python 3.7 or higher <br>
**Required Packages:** pyrealsense2, opencv-python, numpy 
#### Steps 
If you have python, pip, and git already installed skip to step 4 and onward. <br>
1. Download and install the latest version of python from the download section of https://python.org <br>
2. To install pip, run
```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
Note: if you don't have curl installed, download the file from your browser by visiting (https://bootstrap.pypa.io/get-pip.py). Navigate to the downloaded folder using 'cd' command and run the following command to install pip: `python get-pip.py` <br>
3. Install git by downloading the appropriate git installation file from (https://git-scm.com/download/win) and run the executable file. <br>
4. To install Pyrealsense, run
```shell
pip install pyrealsense2
```
5. To install opencv, run
```shell
pip install opencv-python
```
6. To install numpy, run
```shell
pip install numpy
```
7. To collect dataset in TUM format, clone the following directory (https://github.com/Sebastian-Garcia/LEANTumDatasetCollection.git)
```shell
clone git https://github.com/Sebastian-Garcia/LEANTumDatasetCollection.git
```
Once downloaded navigate to its src directory using 'cd' command and run
```bash 
python ThreadStream.py
```
8. To stop the program press Ctrl + C on your terminal <br>
**Note:** You will find a folder named ZoomOut in the src directory containing your data. Be sure to rename it before running the program again to avoid replacing/ losing your data

## 2. Uncertainty Estimation
**System Requirements:** Ubuntu 18.04 or higher, Python 3.8 and PyTprch 1.8.0, and Conda or miniconda <br> 
#### Steps 
1. Download and install the latest version of python from the download section of https://python.org
2. Download Miniconda installation file appropriate to your system. For this project `Miniconda3-py311_23.5.2-0-Linux-x86_64.sh` was used. Then run,
```shell
bash Miniconda3-py311_23.5.2-0-Linux-x86_64.sh
```
Check if properly installed using `conda list`. If correctly installed, a list of packages installed will appear. 
3. Create a virtual environment to install your packages on a virtual environment rather than the base terminal. Run the following
```shell
conda create --name <name> # replace <name> with your desired virtual environment name
conda deactivate # to deactivate virtual environment
```
4. Clone uncertainty estimation algorithm directory from GitHub using the following command
```bash
clone git https://github.com/soumya-ss/uncertainty_from_motion
```
**Note:** If you are using a remote server, follow steps on this ‘Cloning with HTTPS URLs’ github article (https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls). For security, generate a personal access token by following the steps on this ‘Managing your personal access tokens’ github article (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and use generated token instead github password during authentication. 
5. Follow instructions on the ReadMe file from the `uncertainty_from_motion` directory.
6. To use VS-code for remote ssh, follow steps outlined on this ‘Remote Developement using SSH’ article from Visual Studio-code (https://code.visualstudio.com/docs/remote/ssh#:~:text=The%20Visual%20Studio%20Code%20Remote,anywhere%20on%20the%20remote%20filesystem.) 

## 3. Data Visualization
**System Requirements:** Ubuntu 18.04 or higher, Python

#### Steps
1. For visualizing rgb and depth images as separate videos run
```shell
ffmpeg -framerate 30 -pattern_type glob -i '*.png' -c:v libx264 PATH_TO_VIDEO_FOLDER/output_video.mp4
```
Replace PATH_TO_VIDEO_FOLDER with a directory path you want you video to be saved in. **Note:** If you don't have ffmpeg installed, run `sudo apt install ffmpeg`. <br>
2. To view rgb and depth videos side by side, clone this directory by running `git clone https://github.com/Mahderekal/LEANDataCollectionPipeline.git`. Once downloaded,`cd` to that directory run `python adjacent_visualization` or `python3 adjacent_visualization` depending which verion of python you have installed. Then, replace path 'rgb_path', 'depth_path', and 'output_video' path for your input rgb and depth images and output video, respectively. <br>
3. To view an overlay of rgb and depth video, clone this directory by running `git clone https://github.com/Mahderekal/LEANDataCollectionPipeline.git`.Once downloaded,`cd` to that directory run `python overlay_visualization` or `python3 overlay_visualization` depending which verison of python you have installed. Then, replace path 'rgb_path', 'depth_path', and 'output_video' path for your input rgb and depth images and output video, respectively.


## Citations
<a id="1">[1]</a> 
Sudhakar, Soumya, Vivienne Sze, and Sertac Karaman. "Uncertainty from Motion for DNN Monocular Depth Estimation." Under review for 2022 IEEE International Conference on Robotics and Automation (ICRA). (https://github.com/soumya-ss/uncertainty_from_motion.git)
