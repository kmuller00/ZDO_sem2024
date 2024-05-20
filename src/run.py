#!/usr/bin/env python
# coding: utf-8

# In[2]:


import argparse
import skimage
import skimage.io
from skimage import io, color
from scipy import ndimage
from skimage import exposure
from skimage.transform import resize
import os
import skimage.morphology
import skimage.measure
from skimage.morphology import binary_erosion, binary_dilation, rectangle
import scipy
import scipy.ndimage
from scipy.ndimage import binary_erosion, binary_dilation, binary_closing, binary_opening, generate_binary_structure
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.filters import threshold_otsu
import pandas as pd


def detekce_svu_complex_morpho(img, visual):
    desired_width = 60
    desired_height = 150 
    resized_img = resize(img, (desired_width, desired_height), anti_aliasing=True)
    edge_roberts = skimage.filters.roberts(resized_img)
    nhanced_image = exposure.equalize_adapthist(edge_roberts, clip_limit=0.01)
    threshold = np.mean(nhanced_image)

    binary_image = nhanced_image > threshold*1.5
    kernel_big = skimage.morphology.rectangle(1,4)
    binary_image2 = skimage.morphology.binary_dilation(binary_image, kernel_big)
    label_image = skimage.morphology.label(binary_image2)
    regions = skimage.measure.regionprops(label_image)
    largest_region = max(regions, key=lambda r: r.area)
    largest_object = np.zeros_like(binary_image)
    largest_object[label_image == largest_region.label] = 1
    kernel_big = skimage.morphology.rectangle(1,4)
    largest_object2 = skimage.morphology.binary_erosion(largest_object, kernel_big)
    kernel_big = skimage.morphology.rectangle(4,2)
    largest_object3 = skimage.morphology.binary_dilation(largest_object2, kernel_big)
    kernel_big = skimage.morphology.rectangle(29,3)
    lines = scipy.ndimage.binary_erosion(largest_object3, kernel_big, iterations=1)
    regions = skimage.morphology.label(lines)
    num_objects = np.max(regions)
    if visual:
        plt.figure()
        plt.imshow(resized_img, cmap='gray')
        plt.title('resized imgage')
        plt.show()
        plt.figure()
        plt.imshow(edge_roberts, cmap='gray')
        plt.title('edge roberts image')
        plt.show()
        plt.figure()
        plt.imshow(nhanced_image, cmap='gray')
        plt.title('enhanced edge roberts image')
        plt.show()
        plt.figure()
        plt.imshow(binary_image, cmap='gray')
        plt.title('binary image from enhanced edge roberts')
        plt.show()
        plt.figure()
        plt.imshow(binary_image, cmap='gray')
        plt.title('binary image from enhanced edge roberts')
        plt.show()
        plt.figure()
        plt.imshow(binary_image2, cmap='gray')
        plt.title('binary image after binary dilation')
        plt.show()
        plt.figure()
        plt.imshow(largest_object, cmap='gray')
        plt.title('largest object binary image')
        plt.show()
        plt.figure()
        plt.imshow(largest_object2, cmap='gray')
        plt.title('largest object after binary erosion')
        plt.show()
        plt.figure()
        plt.imshow(largest_object3, cmap='gray')
        plt.title('new largest object after binary dilation')
        plt.show()
        plt.figure()
        plt.imshow(lines, cmap='gray')
        plt.title('longest vertical lines')
        plt.show()
    return(num_objects)


def main(args):
    file_list = args.image_files
    v=args.v
    output_path=args.output_path
    counts_complex_mor=[]
    for file_name in file_list:
        image = io.imread(file_name, as_gray=True)
        counts_complex_mor.append(detekce_svu_complex_morpho(image,v))
    data = {
        'filename': file_list,
        'n_stiches': counts_complex_mor,
    }
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument("output_path", type=str)
    parser.add_argument("--v","--visualize", action="store_true")
    parser.add_argument("image_files",type=str, nargs="+", help="List of image files")
    args = parser.parse_args()
    print(args)
    main(args)


# In[ ]:




