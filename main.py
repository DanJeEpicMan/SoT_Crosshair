from PIL import Image
from PIL import ImageGrab
import time
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import win32gui
import win32con
import keyboard

root = Tk()



def task():
    monitor_raw = ImageGrab.grab()
    monitor = monitor_raw.convert("RGB")

    
    

    
    ammo5 = monitor.getpixel((2230,1348))
    if not ammo5 == (173, 255, 171): #if ammo 5 missing check ammo4
        ammo_chart = "4"

        ammo4 = monitor.getpixel((2260,1348))#if ammo 4 missing check ammo 3
        if not ammo4 == (173, 255, 171):
            ammo_chart = "3"

            ammo3 = monitor.getpixel((2300,1348))#if ammo 3 missing check  ammo 2
            if not ammo3 == (173, 255, 171):
                ammo_chart = "2"
                
                ammo2 = monitor.getpixel((2330,1348))#ext ext
                if not ammo2 == (173, 255, 171):
                    ammo_chart = "1"

                    ammo1 = monitor.getpixel((2360,1348))
                    if not ammo1 == (173, 255, 171):
                        ammo_chart = "0"


    else:
        ammo_chart = "5"

    health10 = monitor.getpixel((511,1307))
    if not health10 == (67, 239, 136):
        health_chart = 100

        health9 = monitor.getpixel((483,1307))
        if not health9 == (67, 239, 136):
            health_chart = 90

            health8 = monitor.getpixel((459,1307))
            if not health8 == (67, 239, 136):
                health_chart = 80

                health7 = monitor.getpixel((428,1307))
                if not health7 == (67, 239, 136):
                    health_chart = 70

                    health6 = monitor.getpixel((403,1307))
                    if not health6 == (67, 239, 136):
                        health_chart = 60

                        health5 = monitor.getpixel((376,1307)) # turns read at 340, 1308 (338, 1807)
                        if not health5 == (67, 239, 136):
                            health_chart = 50

                            health4 = monitor.getpixel((344,1307)) #green
                            if not health4 == (67, 239, 136):
                                health_chart = 40

                                health3 = monitor.getpixel((320,1307)) #red
                                if not health3 == (255, 55, 69):
                                    health_chart = 30

                                    health2 = monitor.getpixel((292,1307)) #red
                                    if not health2 == (255, 55, 69):
                                        health_chart = 20

                                        health1 = monitor.getpixel((261,1307)) #red
                                        if not health1 == (255, 55, 69):
                                            health_chart = 10

                                            health_check = monitor.getpixel((180,1292))
                                            #print(health_check)
                                            if not health_check == (67, 239, 136):# ''or (34, 79, 61):
                                                    health_chart = 100
                                                    

                        








                                     #health_1 = monitor.getpixel((180,1322))
                                       #if not health_1 == (173, 255, 171) or (249, 54, 67):
                                       #    health_chart = "1"

    print(ammo_chart)
    print(health_chart)

    '''    var1 = input('image 1 [y/n]')

    if var1 == 'n':
        image1 = Image.open("v2/images/1.1.png")

    if var1 == 'y':
        image1 = Image.open("v2/images/1.0.png")'''

    if ammo_chart == '5':
        image1 = Image.open("v2/images/4.5.png")
    
    if ammo_chart == '4':
        image1 = Image.open("v2/images/4.4.png")

    if ammo_chart == '3':
        image1 = Image.open("v2/images/4.3.png")

    if ammo_chart == '2':
        image1 = Image.open("v2/images/4.2.png")

    if ammo_chart == '1':
        image1 = Image.open("v2/images/4.1.png")

    if ammo_chart == '0':
        image1 = Image.open("v2/images/4.0.png")

    if ammo_chart == '5' and health_chart <= 80:
        image1 = Image.open("v2/images/3.5.png")
    
    if ammo_chart == '4' and health_chart <= 80:
        image1 = Image.open("v2/images/3.4.png")

    if ammo_chart == '3' and health_chart <= 80:
        image1 = Image.open("v2/images/3.3.png")

    if ammo_chart == '2' and health_chart <= 80:
        image1 = Image.open("v2/images/3.2.png")

    if ammo_chart == '1' and health_chart <= 80:
        image1 = Image.open("v2/images/3.1.png")

    if ammo_chart == '0' and health_chart <= 80:
        image1 = Image.open("v2/images/3.0.png")


    if ammo_chart == '5' and health_chart <= 60:
        image1 = Image.open("v2/images/2.5.png")
    
    if ammo_chart == '4' and health_chart <= 60:
        image1 = Image.open("v2/images/2.4.png")

    if ammo_chart == '3' and health_chart <= 60:
        image1 = Image.open("v2/images/2.3.png")

    if ammo_chart == '2' and health_chart <= 60:
        image1 = Image.open("v2/images/2.2.png")

    if ammo_chart == '1' and health_chart <= 60:
        image1 = Image.open("v2/images/2.1.png")

    if ammo_chart == '0' and health_chart <= 60:
        image1 = Image.open("v2/images/2.0.png")


    if ammo_chart == '5' and health_chart <= 30:
        image1 = Image.open("v2/images/1.5.png")
    
    if ammo_chart == '4' and health_chart <= 30:
        image1 = Image.open("v2/images/1.4.png")

    if ammo_chart == '3' and health_chart <= 30:
        image1 = Image.open("v2/images/1.3.png")

    if ammo_chart == '2' and health_chart <= 30:
        image1 = Image.open("v2/images/1.2.png")

    if ammo_chart == '1' and health_chart <= 30:
        image1 = Image.open("v2/images/1.1.png")

    if ammo_chart == '0' and health_chart <= 30:
        image1 = Image.open("v2/images/1.0.png")


    #make gui
    test = ImageTk.PhotoImage(image1)
    root.geometry("2560x1440")
    root.attributes('-transparentcolor','#f0f0f0')

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=1230, y=635)

    if keyboard.is_pressed("alt+q"):
        hwnd = win32gui.GetForegroundWindow()#          xpos ypos width hight importance
        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,2560,1440,0)
    if keyboard.is_pressed("alt+e"):
        hwnd = win32gui.FindWindow(None, "tk") # Getting window handle
        # hwnd = root.winfo_id() getting hwnd with Tkinter windows
        # hwnd = root.GetHandle() getting hwnd with wx windows
        lExStyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        lExStyle |=  win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE , lExStyle )



    root.after(200, task)  # reschedule event in 2 seconds



root.after(500 , task)
root.mainloop()