#import required modules
import PySimpleGUI as sg
import os
import PIL
from PIL import Image, ImageTk
import io
import sys
import time
import cv2
from PIL import Image
import glob

# Get the file for test image
sg.theme('DarkBrown 2')
if len(sys.argv)==1:
    fname = sg.popup_get_file('Select Image To Use as TestImage', default_path='')
    image_cv2 = cv2.imread(fname)
    #saving image to test folder
    result = cv2.imwrite(r'testimage/testimage.png', image_cv2)
    #converting test image and saving as thumbnail
    image = Image.open('testimage/testimage.png')
    image.thumbnail((110,110))
    image.save('testimage/testimagethumbnail.png')
    #converting frame 5 captured and saving as randomimage
    image = Image.open('5.png')
    image.thumbnail((110,110))
    image.save('testimage/framethumbnail.png')
    #converting test image for display
    image = Image.open('testimage/testimage.png')
    image.thumbnail((250,250))
    image.save('testimage/viewtest.png')
    
    if result == True:
        sg.popup_auto_close("Test Image Saved")
    else:
        sg.popup_auto_close("Test Image Not Saved!!!")


