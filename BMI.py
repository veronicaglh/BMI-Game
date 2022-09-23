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

# Placing the widgets of window1
label_1.place(x=370, y=120)
label_2.place(x=450, y=160)
get_biological_sex.place(x=370, y=210)
get_biological_sex_entry.place(x=472, y=212)
get_weight.place(x=370, y=242)
get_weight_entry.place(x=472, y=246)
get_height.place(x=370, y=272)
get_height_entry.place(x=472, y=276)
game_mode_button.place(x=430, y=305)
calculate_button.place(x=525, y=305)
# ~~~~~~~~~~~~~~~~ end of window1 ~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~ window2 ~~~~~~~~~~~~~~~~
# Since the background image has already been loaded(in window1)
# we do not need to load it again
img = Label(window2, image=render)
img.place(x=0, y=0)

calculate_title = Label(window2, text='Calculate', bg='#DAF3F0',fg='black',font=('Modern', 25, 'bold'))
result_label = Label(window2, text='Result:', bg='#DAF3F0',fg='#535353', font=('Calibri', 13, 'normal'))
result_text_box = Text(window2, height=8, width=25, wrap=WORD, highlightthickness=2)
result_text_box.config(highlightcolor='#DAF3F0')

back_button = Button(window2, text='Back',fg='#535353',font=('Calibri', 12, 'normal'), command=lambda: show_frame(window1))
back_button. config(width=8)

# Placing the widgets of window 2
calculate_title.place(x=410, y=120)
result_label.place(x=415, y=170)
result_text_box.place(x=415,y=200)
back_button.place(x=545, y=340)
# ~~~~~~~~~~~~~~~~ end of window2 ~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~ window3 ~~~~~~~~~~~~~~~~
img = Label(window3, image=render)
img.place(x=0, y=0)

game_mode_title = Label(window3, text='Game Mode', bg='#DAF3F0',fg='black',font=('Modern', 25, 'bold'))
game_mode_label_a = Label(window3, text='Try guessing your BMI and the program', bg='#DAF3F0',fg='#535353', font=('Calibri', 12, 'normal'))
game_mode_label_b = Label(window3, text="will tell you when you're hot or cold", bg='#DAF3F0',fg='#535353', font=('Calibri', 12, 'normal'))

game_mode_entry = Label(window3, text='Enter your guess below: ', bg='#DAF3F0',fg='#535353', font=('Calibri', 12, 'normal'))
game_mode_entry_box = Entry(window3, highlightthickness=2)
game_mode_entry_box.config(width=30)
game_mode_result = Label(window3, text='Result:', bg='#DAF3F0',fg='#535353', font=('Calibri', 12, 'normal'))
game_mode_result_text_box = Text(window3, height=5, width=25, wrap=WORD, highlightthickness=2)
game_mode_result_text_box.config(highlightcolor='#DAF3F0')


# Placing the widgets of window 3
game_mode_title.place(x=410, y=120)
game_mode_label_a.place(x=415, y=160)
game_mode_label_b.place(x=415, y=180)
game_mode_entry.place(x=415, y=200)
game_mode_entry_box.place(x=415, y=225)
game_mode_result.place(x=415, y=260)
game_mode_result_text_box.place(x=415, y=280)
# ~~~~~~~~~~~~~~~~ end of window3 ~~~~~~~~~~~~~~~~
