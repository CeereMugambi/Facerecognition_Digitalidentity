import PySimpleGUI as sg
import os
import cv2
from PIL import Image, ImageTk
from PIL import Image



def govt_input():
    sg.theme('DarkBrown 2')

    # Very basic window.
    # Return values using
    # automatic-numbered keys
    layout = [
        [sg.Text('Please enter your ID Number')],
        [sg.Text('ID Number', size=(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('ID Input Window', layout)
    event, values = window.read()
    window.close()

    # The input data looks like a simple list
    # when automatic numbered
    id_num = values[0]
    print(id_num,type(id_num))
    return id_num
    #print(event)

def check_govt_image_db(id_number):
    govt_image_db = 'government_repository'  # dummy folder rep govt db of images

    for filename in os.listdir(govt_image_db):
        #print(f'Filenames are:- {filename}')
        if filename.startswith(id_number):
            sg.theme("DarkGreen")
            sg.popup("User found")
#
            print('User found')
            p = filename
    return p
        


id_number = govt_input()

p = check_govt_image_db(id_number)


image_path = f'government_repository/{p}'
image_cv2 = cv2.imread(image_path)
#saving image to test folder
saved_govt_img = cv2.imwrite(r'testimage/testimage.png', image_cv2)

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




