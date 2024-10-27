#!/usr/bin/env python3
import numpy as np

def convolve_grayscale_valid(images, kernel):
    # Get dimensions of the images and the kernel
    m, h, w = images.shape
    kh, kw = kernel.shape
 
    # Calculate output dimensions
    output_height = h - kh + 1
    output_width = w - kw + 1
    
    # Initialize the output array
    convolved_images = np.zeros((m, output_height, output_width))
    
    # Perform convolution
    for i in range(m):  # Loop over images
        for y in range(output_height):  # Loop over output height
            for x in range(output_width):  # Loop over output width
                # Apply kernel to the current patch of the image
                convolved_images[i, y, x] = np.sum(
                    images[i, y:y + kh, x:x + kw] * kernel
                )
    
    return convolved_images
