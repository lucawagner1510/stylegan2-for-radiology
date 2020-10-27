# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:04:03 2020

@author: luca_
"""

#!/usr/bin/python


import pydicom as dicom
import os
import cv2
import PIL
from PIL import Image
count=0
im_size=256
outdir='D:\data\mammography_dataset\data'

# traverse root directory, and list directories as dirs and files as files
# for root, dirs, files in os.walk("D:\data\mammography_dataset\CBIS-DDSM"):
#     #path = root.split(os.sep)
#     #print((len(path) - 1) * '---', os.path.basename(root))
#     for file in files:
#         #print(len(path) * '---', file)
#         ds = dicom.dcmread(os.path.join(root, file))
#         pixel_array_numpy = ds.pixel_array
#         filename_zero, fileext = os.path.splitext(file)
#         file = file.replace(filename_zero, 'img_' +str(count))
#         file = file.replace('.dcm', '.png')
#         cv2.imwrite(os.path.join(outdir, file), pixel_array_numpy)
#         count+=1
        


import numpy as np


def resizeAndPad(img, size, padColor=0):

    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    # aspect ratio of image
    aspect = w/h  # if on Python 2, you might need to cast as a float: float(w)/h

    # compute scaling and pad sizing
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
        pad_vert = (sh-new_h)/2
        pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
        pad_left, pad_right = 0, 0
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
        pad_horz = (sw-new_w)/2
        pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
        pad_top, pad_bot = 0, 0
    else: # square image
        new_h, new_w = sh, sw
        pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

    # set pad color
    if len(img.shape) is 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
        padColor = [padColor]*3

    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)

    return scaled_img


    
for root, dirs, files in os.walk(outdir):
    for file in files: 
        #img = Image.open(os.path.join(root, file))
        img =cv2.imread(os.path.join(root, file))
        img = resizeAndPad(img, (im_size, im_size), 255)
               
        print('write image...' +str(count))
        #img.save(os.path.join('D:\data\mammography_dataset\resized', 'img_resized_'+str(count)+'.png'))
        cv2.imwrite(os.path.join('D:\data\mammography_dataset\_resized', 'img_resized_'+str(count)+'.png'), img) 
        count+=1
        
