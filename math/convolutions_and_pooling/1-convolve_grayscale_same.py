#!/usr/bin/env python3
""" convolution on grayscale images with custom padding"""

import numpy as np

def convolve_grayscale_padding(images, kernel, padding):
    # Get dimensions of the images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    # Calculate output dimensions
    output_height = h + 2 * ph - kh + 1
    output_width = w + 2 * pw - kw + 1
    
    # Initialize padded images
    padded_images = np.zeros((m, h + 2 * ph, w + 2 * pw))
    
    # Fill in the padded images
    padded_images[:, ph:ph + h, pw:pw + w] = images

    # Initialize output array for convolved images
    convolved_images = np.zeros((m, output_height, output_width))
    
    # Perform convolution
    for i in range(m):  # Loop over images
        for y in range(output_height):  # Loop over output height
            for x in range(output_width):  # Loop over output width
                # Apply kernel to the current patch of the padded image
                convolved_images[i, y, x] = np.sum(
                    padded_images[i, y:y + kh, x:x + kw] * kernel
                )
    
    return convolved_images
