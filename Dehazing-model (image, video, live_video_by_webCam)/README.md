# Image Dehazing Project

## Overview

The Image Dehazing Project provides an algorithm to remove haze from images using advanced techniques like airlight estimation, boundary constraints, and transmission refinement. Built with Python and OpenCV, this project restores clarity to hazy images by estimating the atmospheric light, refining the transmission map, and applying edge-detection filters for enhanced dehazing results. This process improves the visual quality of images taken in conditions where haze or fog is present, making it suitable for applications in photography, satellite imagery, and computer vision.

## Features

This project offers several key features to tackle haze removal:

- **Airlight Estimation:** Calculates the atmospheric light using local window operations.
- **Boundary Constraints:** Applied to estimate haze levels, helping to refine the transmission map.
- **Edge Detection:** A Kirsch filter bank is used to compute edges and improve the map.
- **Transmission Refinement:** The transmission is optimized through iterative methods.
- **Customizable Parameters:** Adjustable parameters to fine-tune the process for different images.

The result is a dehazed image and a corresponding transmission map, which can be customized with adjustable parameters, allowing users to fine-tune the process for various images.

## Installation

### Clone the repository:

**git clone https://github.com/your-username/image-dehazing.git**
**cd image-dehazing**


Install required dependencies: **pip install numpy opencv-python**

## File Structure
__init__.py: Contains the image_dehazer class with all the necessary methods for dehazing.
main.py: The main script for loading images, running the dehazing algorithm, and displaying results.

## Usage
To use the project as a standalone script, simply place your hazy image in the project directory and run python main.py. The script will display both the dehazed image and the corresponding transmission map. If you want to use the dehazing functionality in your own Python project, you can import the remove_haze function from image_dehazer and pass a hazy image to it, obtaining the dehazed result and transmission map as output.

## Parameters
Several parameters can be adjusted to optimize the dehazing process. These include the window sizes for airlight estimation and boundary constraints, regularization values, and fine-tuning parameters such as sigma and delta. Users can tweak these parameters to achieve the best results depending on the input image characteristics.

## Output
The main outputs of the algorithm are the dehazed image, which is the primary result of haze removal, and the haze transmission map, which shows the estimated haze levels across the image. These results provide a clearer representation of the scene, enhancing visibility and image quality.

## Notes
Ensure the input images are in formats like .jpg or .png. Feel free to adjust the parameters to optimize dehazing for different images. The project is designed to be flexible and can be adapted to various real-world use cases involving hazy or foggy imagery.
