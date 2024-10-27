#!/usr/bin/env python3
"""Module for performing valid convolution on grayscale images"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Parameters:
        images: numpy.ndarray with shape (m, h, w) containing multiple grayscale images
            m is the number of images
            h is the height in pixels of the images
            w is the width in pixels of the images
        kernel: numpy.ndarray with shape (kh, kw) containing the convolution kernel
            kh is the height of the kernel
            kw is the width of the kernel
       
    Returns:
        numpy.ndarray containing the convolved images
    """
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
 
    # Calculate output dimensions for valid convolution
    output_h = h - kh + 1
    output_w = w - kw + 1
    
    # Initialize output array
    output = np.zeros((m, output_h, output_w))

    # Perform convolution for each image
    for i in range(m):
        # Slide kernel over each position in the image
        for j in range(output_h * output_w):
            # Convert flat index j to 2D coordinates
            row = j // output_w
            col = j % output_w

            #perform element-wise multiplication with kernel
            current_window = images[i, row:row + kh, col:col + kw]
            output[i, row, col] = np.sum(current_window * kernel)
        
    return output