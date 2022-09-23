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


# ~~~~~~~~~~~~~~~~ window1 ~~~~~~~~~~~~~~~~
# Declaring the widgets of window1
load = Image.open('Images\\BMI_Background_Image_4.jpg')
render = ImageTk.PhotoImage(load)
img = Label(window1, image=render)
img.place(x=0, y=0)

label_1 = Label(window1, text='⟢ Calculate your BMI ⟢', bg='#DAF3F0',fg='black',font=('Modern', 25, 'bold'))
label_2 = Label(window1, text='Fill in the form below', bg='#DAF3F0',fg='#535353',font=('Calibri', 10, 'normal'))

get_biological_sex = Label(window1, text='Biological Sex:',bg='#DAF3F0',fg='#535353', font=('Calibri', 12, 'normal'))
get_biological_sex_entry = Entry(window1, highlightthickness=2)

get_weight = Label(window1, text='Weight (in kg):',bg='#DAF3F0',fg='#535353', font=('Calibri', 12, 'normal'))
get_weight_entry = Entry(window1, highlightthickness=2)

get_height = Label(window1, text='Height (in m):',bg='#DAF3F0',fg='#535353', font=('Calibri', 13, 'normal'))
get_height_entry = Entry(window1, highlightthickness=2)

calculate_button = Button(window1, text='Calculate',fg='#535353',font=('Calibri', 12, 'normal'), command=lambda: show_frame(window2))
calculate_button. config(width=8)

game_mode_button = Button(window1, text='Game Mode',fg='#535353',font=('Calibri', 12, 'normal'), command=lambda: show_frame(window3))
game_mode_button. config(width=10)

