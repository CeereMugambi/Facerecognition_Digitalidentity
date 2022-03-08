import cv2
import time
import numpy as p
import PySimpleGUI as sg
import subprocess
import logzero
from logzero import logger
from PIL import Image
import glob
import sys
import PIL
from PIL import Image, ImageTk


def confirm_window():
    sg.theme('DarkBrown 2')
    layout_column= [
    [sg.Text("Confirmation Window" ,justification="centre",size=(30, 1),font=("Helvetica", 25))],
    [sg.Text('_'  * 80)],
    [sg.Text("This application is used for identity verification")],
    [sg.Text("Do you have ypur identification card",justification= "centre")] ,
    [sg.Button("I do",size=(10, 1), key = "Continue")],
    [sg.Button("I do not",size=(10, 1), key = "Continue2")] ,
    #sg.Button("Exit", size=(10, 1),key = "Exit")],
    [sg.Text('_'  * 100)],
    [sg.Text('_'  * 100)]
    ]

    pagelayout = [[sg.Column(layout_column, element_justification='center')]]

    rowfooter = [[sg.Image(filename="equitylogo1.png",size= (700,200), key="-IMAGEBOTTOM-"),sg.Text('  ')],
                [sg.Text("© Equity Bank Limited",justification= "centre")]
                ]
    footerlayout = [[sg.Column(rowfooter, element_justification = 'centre')]]

    layout = [pagelayout, footerlayout]

    window = sg.Window("Confirmation Window", layout, size=(750,450))


    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == "Continue":
            select_testimage()

        if event == "Continue2":
         sp = subprocess.Popen( "search_image.py", shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=None)
        out, err = sp.communicate()
        if out:
                print(out.decode("utf-8"))
        if err:
                print(err.decode("utf-8"))

        window.close()
        prog_window()



def selected_testimage():
    sg.theme('DarkBrown 2')
    layout_column= [
    [sg.Text("Chosen Test Image" ,justification="centre",size=(30, 1),font=("Helvetica", 25))],
    [sg.Text('_'  * 80)],
    [sg.Image(filename=r"testimage/viewtest.png", key="-IMAGETEST-")],
    [sg.Text("Choosen Image to be Used As Test Image",justification = "centre")],
    [sg.Button("Continue To Analysis",size=(10, 3), key = "Continue")],
    [sg.Text('_'  * 100)],
    [sg.Text('_'  * 100)]
    ]

    pagelayout = [[sg.Column(layout_column, element_justification='center')]]

    rowfooter = [[sg.Image(filename="equitylogo1.png", size= (700,200),key="-IMAGEBOTTOM-"),sg.Text('  ')],
                [sg.Text("© Equity Bank Limited",justification= "centre")]
                ]
    footerlayout = [[sg.Column(rowfooter, element_justification = 'centre')]]

    layout = [pagelayout, footerlayout]

    window = sg.Window("Test Image Page-Face API", layout, modal = True)

    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
        if event == "Continue":
            window.close()
            prog_window()

def select_testimage():
    sg.theme('DarkBrown 2')
    layout_column= [
    [sg.Text("Pick TestImage" ,justification="centre",size=(30, 1),font=("Helvetica", 25))],
    [sg.Text('_'  * 80)],
    [sg.Text("Choose Image to be Used As Test Image",justification = "centre")],
    [sg.B('Choose',size=(10, 1), key = 'Choose')],
    [sg.Text('_'  * 100)],
    [sg.Text('_'  * 100)]
    ]

    pagelayout = [[sg.Column(layout_column, element_justification='center')]]

    rowfooter = [[sg.Image(filename="equitylogo1.png", size= (700,200),key="-IMAGEBOTTOM-"),sg.Text('  ')],
                [sg.Text("© Equity Bank Limited",justification= "centre")]
                ]
    footerlayout = [[sg.Column(rowfooter, element_justification = 'centre')]]

    layout = [pagelayout, footerlayout]

    window = sg.Window("Test Image Page-Face API", layout, modal = True)

    while(True):
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "Choose":
            sp = subprocess.Popen( "filebrowse.py", shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=None)
            out, err = sp.communicate()
            if out:
                print(out.decode("utf-8"))
            if err:
                print(err.decode("utf-8"))

        window.close()
        selected_testimage()

def prog_window():
    sg.theme('DarkBrown 2')
    x=0
    layout_column= [
    [sg.Text("MS Face Application",size=(30, 1),font=("Helvetica", 25), key = "new")],
    [sg.Text('_'  * 80)],
    [sg.Text("Press Run button")],
    [sg.Text('Random Frame'),sg.Text(' ' * 10),sg.Text('Test Image')],
    [sg.Image(filename=r"testimage/framethumbnail.png", key="-IMAGETAKEN-"),sg.Text('  ' * 5), sg.Image(filename=r"testimage/testimagethumbnail.png", key="-TESTIMAGE-")],
    [sg.ProgressBar(1,orientation='h', size=(40,20),key='progress2')],
    [sg.Output(size=(80, 20))],
    [sg.Button("RUN", size=(10, 1),key = "RUN")],
    [sg.Button("Exit", key = "Close")],
    [sg.Text('_'  * 80)]
    ]

    layout1 = [[sg.Column(layout_column, element_justification='center')]]

   

    layout = [layout1]  #, footerlayout
    window = sg.Window("Face matching", layout, modal = True)
    progress_bar2 = window.find_element('progress2')
    while(True):
        event, values = window.read()
        if event == "Close" or event == sg.WINDOW_CLOSED:
            window.close()
            main()
            break
        elif event == "RUN":
            progress_bar2.UpdateBar(x, 5)
            print("This will take less than a minute(depending on you internet speed)" + ". . . . .")
            x=1
            start = time.process_time()
            time.sleep(2)
            progress_bar2.UpdateBar(x, 5)
            print("Analysis in progress ...")
            time.sleep(2)
            print("...")
            logzero.logfile("logfile.log", maxBytes=1e6, backupCount=3, disableStderrLogger=True)
            sp = subprocess.Popen( "facerecognition.py", shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=None)
            x=3
            progress_bar2.UpdateBar(x, 5)
            out, err = sp.communicate()
            if out:
                x=5
                progress_bar2.UpdateBar(x, 5)
                print(out.decode("utf-8"))
                logger.info(out)
            if err:
                x=5
                progress_bar2.UpdateBar(x, 5)
                print(err.decode("utf-8"))
                logger.info(err)

            
            #print('Face Analysis Took','---%s seconds---'% (time.process_time() - start))

    #window.close()



def webcam_window():
    
    # Camera Settings
    camera_Width  = 640 # 480 # 640 # 1024 # 1280
    camera_Heigth = 480 # 320 # 480 # 780  # 960
    frameSize = (camera_Width, camera_Heigth)
    video_capture = cv2.VideoCapture(0)
    i = 0
    # init Windows Manager
    sg.theme("DarkBrown 2")

    # def webcam col
    colwebcam1_layout = [[sg.Text("Camera View", size=(30, 1),font=("Helvetica", 25), justification="center")],
                        [sg.Text('_'  * 100)],
                        [sg.Text('Ensure you are in a well lit room',size = (30,1), font = ('Any 15'))],
                        [sg.Text("Capturing Frames" + " .  " *5 , size = (30, 1), font=('Any 15'))],
                        [sg.Text("Change Pose after every 1 second" , size=(30, 1), font=('Any 15'))],
                        [sg.Text('In progress ...' , size=(30, 1), font=('Any 15'))],
                        [sg.ProgressBar(1,orientation='h', size=(40,20),key='progress')],
                        [sg.Image(filename="", key="cam1")],
                        [sg.Text('_'  * 100)]
                        ]
    colwebcam1 = sg.Column(colwebcam1_layout, element_justification='center')

    colslayout = [colwebcam1]

    layout = [colslayout]

    window    = sg.Window("Face API Video Capture", layout, 
                        no_titlebar=False, alpha_channel=1, grab_anywhere=False, 
                        return_keyboard_events=True, size=(750, 550), modal = True)
    progress_bar = window.find_element('progress')
    while(True):
        start_time = time.time()   
        event, values = window.read(timeout=20)
        time.sleep(1)

        if event == sg.WIN_CLOSED:
            break

        # get camera frame
        ret, frameOrig = video_capture.read()
        time.sleep(1)
        frame = cv2.resize(frameOrig, frameSize)
        # Save Frame by Frame into disk using imwrite method
        cv2.imwrite(str(i) +'.png', frame)
        i += 1
        progress_bar.UpdateBar(i, 13)
        # # update webcam1
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["cam1"].update(data=imgbytes)
        
        if i > 13:
            #print("Horray!!Photo capture complete")
            video_capture.release()
            window.close()
            confirm_window()
           #select_testimage()
           

    cv2.destroyAllWindows()

    
def main():
    sg.theme('DarkBrown 2')
    layout_column= [
    [sg.Text("Welcome to MS Face API Application" ,justification="centre",size=(30, 1),font=("Helvetica", 25))],
    [sg.Text('_'  * 80)],
    [sg.Text("This application is used for identity verification")],
    [sg.Text("Press 'START' to start application",justification= "centre")] ,
    [sg.Button("Start",size=(10, 1), key = "Start")] ,
    #sg.Button("Exit", size=(10, 1),key = "Exit")],
    [sg.Text('_'  * 100)],
    [sg.Text('_'  * 100)]
    ]

    pagelayout = [[sg.Column(layout_column, element_justification='center')]]

    rowfooter = [[sg.Image(filename="equitylogo1.png",size= (700,200), key="-IMAGEBOTTOM-"),sg.Text('  ')],
                [sg.Text("© Equity Bank Limited",justification= "centre")]
                ]
    footerlayout = [[sg.Column(rowfooter, element_justification = 'centre')]]

    layout = [pagelayout, footerlayout]

    window = sg.Window("Home Page-Face API", layout, size=(750,450))


    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == "Start":
            #for i in range(10000):
                #sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='green', transparent_color='green',time_between_frames=1000)
        #sg.PopupAnimated(None)
        #confirm_window()
            webcam_window()
            window.close()


        
           

      
            
            
    #window.close()
    
if __name__ == "__main__":
    main()
