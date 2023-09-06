Instructions for Data Collection Pipeline
============

An end-to-end instruction on data collection using Intel RealSense Depth Camera D435i, running uncertainty estimation algorithm using acquired data, and data visualization.

Lab website: [lean.mit.edu](https://lean.mit.edu/)
## Introduction
Traditionally depth estimation is done using depth sensors such as Intel’s D435i, which are large, heavy, and energy-intensive. Low-energy robots on the other hand have limited energy and load-carrying capacity. Therefore, researchers are now using Deep Neural Networks for depth estimation. Even so, it’s hypothesized that models with better generalization capabilities are more energy-intensive and require data to be ready before training. This is not only limiting for low-energy robots but also limits robot performance in real-world scenarios where data is available sequentially. As a solution, in the LEAN lab, we use  small DNN models to train small robots online on the fly. To build more reliable depth estimation DNNs, we use aleatoric (data inherent) and epistemic (model inherent) uncertainty estimation techniques. 

To conduct this research, we collected datasets in interesting and challenging conditions including optical illusion and environment brightness changes. We then run aleatoric and epistemic (ensemble) uncertainty methods from the Uncertainty from Motion algorithm [[1]](#1) on these datasets to qualitatively and quantitatively analyze how both methods perform. This repo contains an end-to-end instruction guide on how to conduct data collection and visualization process as well as running uncertainty estimation methods using the Uncertainty from Motion algorithm. Additionally, it contains adjacent and overlay depth and RGB data visualization programs. 

## Get Started
Instructions for the data collection process on a Windows OS are listed in the first section. These are steps taken to collect RGB and depth data from the Intel RealSense D435i depth sensor on a Windows OS.

**Note:** Currently, PyRealSense does not have a distribution that’s compatible with the new M1 chip Macbook laptops due to its ARM-based architecture. Therefore, if you have an M1 chip Macbook, I recommend that you conduct at least the data collection process on a Windows machine (Windows dual boot with a Linux OS should be fine). In addition, the Realsense library installation is not supported on a Virtual Machine due to the USB 3.0 translation layer between native hardware and the virtual machine, see (https://dev.intelrealsense.com/docs/compiling-librealsense-for-linux-ubuntu-guide) for more details.

Instructions on running uncertainty estimation algorithms on collected data are outlined in the second section followed by data visualization instructions in the third section (both using a Linux OS). 

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
Note: If you don't have curl installed, download the file from your browser by visiting (https://bootstrap.pypa.io/get-pip.py). Navigate to the downloaded folder using 'cd' command and run the following command to install pip: `python get-pip.py` <br>
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
1. Download and install the latest version of Python from the download section of https://python.org
2. Download the Miniconda installation file appropriate to your system. For this project `Miniconda3-py311_23.5.2-0-Linux-x86_64.sh` was used. Then run,
```shell
bash Miniconda3-py311_23.5.2-0-Linux-x86_64.sh
```
Check if properly installed using `conda list`. If correctly installed, a list of packages installed will appear. 
3. Create a virtual environment to install your packages on a virtual environment rather than the base terminal. Run the following
```shell
conda create --name <name> # replace <name> with your desired virtual environment name
conda deactivate # to deactivate the virtual environment
```
4. Clone uncertainty estimation algorithm directory from GitHub using the following command
```bash
clone git https://github.com/soumya-ss/uncertainty_from_motion
```
**Note:** If you are using a remote server, follow the steps in this ‘Cloning with HTTPS URLs’ GitHub article (https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls). For security, generate a personal access token by following the steps on this ‘Managing your personal access tokens’ GitHub article (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and use generated token instead GitHub password during authentication. 
5. Follow instructions on the ReadMe file from the `uncertainty_from_motion` directory.
6. To use VS-code for remote ssh, follow the steps outlined in this ‘Remote Development using SSH’ article from Visual Studio-code (https://code.visualstudio.com/docs/remote/ssh#:~:text=The%20Visual%20Studio%20Code%20Remote,anywhere%20on%20the%20remote%20filesystem.) 

## 3. Data Visualization
**System Requirements:** Ubuntu 18.04 or higher, Python

#### Steps
1. For visualizing RGB and depth images as separate videos run
```shell
ffmpeg -framerate 30 -pattern_type glob -i '*.png' -c:v libx264 PATH_TO_VIDEO_FOLDER/output_video.mp4
```
Replace PATH_TO_VIDEO_FOLDER with a directory path you want your video to be saved in. **Note:** If you don't have ffmpeg installed, run `sudo apt install ffmpeg`. <br>
2. To view RGB and depth videos side by side, clone this directory by running `git clone https://github.com/Mahderekal/LEANDataCollectionPipeline.git`. Once downloaded,`cd` to that directory and run `python adjacent_visualization` or `python3 adjacent_visualization` depending on which version of Python you have installed. Then, replace path 'rgb_path', 'depth_path', and 'output_video' paths for your input rgb and depth images and output video, respectively. <br>
3. To view an overlay of RGB and depth video, clone this directory by running `git clone https://github.com/Mahderekal/LEANDataCollectionPipeline.git`.Once downloaded,`cd` to that directory and run `python overlay_visualization` or `python3 overlay_visualization` depending on which version of Python you have installed. Then, replace path 'rgb_path', 'depth_path', and 'output_video' paths for your input rgb and depth images and output video, respectively.


## Troubleshooting for Uncertainty from Motion Algorithm
1. To install PyTorch and other dependencies, activate the conda environment and run
```shell
conda install pytorch=1.12.0 torchvision=0.13.0 torchaudio=0.12.0 cudatoolkit=11.3 -c pytorch -c conda-forge
```
Once it's complete, `cd` to the cloned uncertainty_from_motion directory and run `./installation.sh` <br>
2. Place your dataset directory outside of the UfM folder and modify the path to the dataset sequence in the config file. Note: Choose a config file that matches your camera requirements or duplicate one of the config files and modify the camera intrinsic. <br>
3. To visualize results or display a video, run the slightly modified visualize_video.py file from this folder. Create a folder where you can save output PNG files and update the output path in the visualize_video.py file accordingly. <br>
4. Once all the images have been saved in the output folder, `cd` there and run `ffmpeg -framerate 30 -i result_%d.png -c:v libx264 -pix_fmt yuv420p output_video.mp4` to convert it to a video. You can replace the name of the output video. <br>
**Additional troubleshooting tips**
- While following the instructions in the UfM readme file add ‘CUDA_VISIBLE_DEVICES=1,2’ on the command for running the UfM (python3 examples/evaluate_uncertainty_network.py configuration/configuration_freiburg4.yaml)
- When plotting the calibration curves, use `multiview` for running UfM, or replace it with `aleatoric` or `epistemic` (which is an ensemble of aleatoric and epistemic) 

## Citations
<a id="1">[1]</a> 
Sudhakar, Soumya, Vivienne Sze, and Sertac Karaman. "Uncertainty from Motion for DNN Monocular Depth Estimation." Under review for 2022 IEEE International Conference on Robotics and Automation (ICRA). (https://github.com/soumya-ss/uncertainty_from_motion.git)
