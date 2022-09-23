# This program will calculate the BMI of a user
# It also had a GUI that has been built with tkinter
# In addition it also has a Game Mode(optional) which lets users
# guess their BMI and the program will tell them when they are hot or cold.
# This program does need the pillow package to work properly
# So if you have not installed that you can install it
# by running the following command on your IDE's terminal
# pip install pillow

import math
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import threading

# TKINTER - GUI
mainWindow = Tk()
mainWindow.geometry('736x414')
mainWindow.rowconfigure(0, weight=1)
mainWindow.columnconfigure(0, weight=1)
mainWindow['background'] = '#DAF3F0'
mainWindow.title("BMI")

# The UI will have 3 different windows
window1 = Frame(mainWindow)
window2 = Frame(mainWindow)
window3 = Frame(mainWindow)

for frame in (window1, window2, window3):
    frame.grid(row=0, column=0, sticky='nsew')
    frame.config(background='#DAF3F0')


# The function show_frame() will display the page when called.
# For eg if page1 is given as an argument(show_frame(window1)) it will display page1
# It will start by displaying window1
def show_frame(frame):
    frame.tkraise()


show_frame(window1)
