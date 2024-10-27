#!/usr/bin/env python3
"""Module for performing valid convolution on grayscale images"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.
    
    Parameters:
        images: numpy.ndarray shape (m, h, w) containing grayscale images
            m is the number of images
            h is the height in pixels of the images
            w is the width in pixels of the images
        kernel: numpy.ndarray with shape (kh, kw) containing kernel
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

    output_h = h - kh + 1
    output_w = w - kw + 1
    output = np.zeros((m, output_h, output_w))

    for i in range(m):
        for y in range(output_h):
            for x in range(output_w):
                output[i, y, x] = np.sum(
                    images[i, y:y + kh, x:x + kw] * kernel
                )

    return output
