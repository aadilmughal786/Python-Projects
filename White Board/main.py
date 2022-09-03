from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from math import floor
from PIL import Image
from os import remove
import tkinter.simpledialog
import webbrowser
from tkinter import colorchooser

root = Tk()
root.title("White Board : By Aadil Mugal")
root.resizable(0, 0)

s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
window_width = floor(s_width*0.8)
window_height = floor(s_height*0.8)
x = int(int(s_width/2) - int(window_width/2))
y = int(int(s_height/2) - int(window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

current_width = 2
current_x = 0
current_y = 0
current_color = "black"


def locate_xy(work):
    global current_x, current_y
    current_x, current_y = work.x, work.y


def addLine(work):
    global current_x, current_y, current_width
    canvas.create_line((current_x, current_y, work.x, work.y),
                       width=current_width, fill=current_color,
                       capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y


def show_color(c):
    global current_color
    current_color = c
    # print(c)


def change_width(w):
    global current_width
    current_width = w


def save_as_png(canvas):
    fileName = tkinter.simpledialog.askstring(
        'Aadil Says', 'Enter file name')
    try:
        # save postscipt image
        canvas.postscript(file=fileName + '.eps')
        # use PIL to convert to PNG
        img = Image.open(fileName + '.eps')
        img.save(fileName + '.png', 'png')
        remove(fileName+".eps")
    except:
        pass


def choose_color():
    global current_color
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    current_color = color_code[1]


# png
logo = PhotoImage(file="./img/logo.png")
root.iconphoto(0, logo)
eraser = PhotoImage(file="./img/eraser.png")
save = PhotoImage(file="./img/save.png")
github = PhotoImage(file="./img/github.png")
cpicker = PhotoImage(file="./img/cpicker.png")


colors = Canvas(root, bg="#ffffff", width=50, height=window_height)
colors.grid(row=0, column=0)


colors_name = ("black", "gray", "brown4", "orange",
               "yellow", "red", "green", "blue", "purple")

start_x = 10
start_y = 10


def display_pallete():
    id = colors.create_rectangle(
        (start_x, 10 + 40*1, 40, 40 + 40*1), fill=colors_name[0])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[0]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*2, 40, 40 + 40*2), fill=colors_name[2])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[2]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*3, 40, 40 + 40*3), fill=colors_name[3])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[3]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*4, 40, 40 + 40*4), fill=colors_name[4])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[4]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*5, 40, 40 + 40*5), fill=colors_name[5])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[5]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*6, 40, 40 + 40*6), fill=colors_name[6])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[6]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*7, 40, 40 + 40*7), fill=colors_name[7])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[7]))
    id = colors.create_rectangle(
        (start_x, 10 + 40*8, 40, 40 + 40*8), fill=colors_name[8])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: show_color(colors_name[8]))

    id = colors.create_rectangle(
        (start_x, 370+10, 40, 372+10), fill=colors_name[0])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: change_width(2))
    id = colors.create_rectangle(
        (start_x, 380+10, 40, 385+10), fill=colors_name[0])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: change_width(5))
    id = colors.create_rectangle(
        (start_x, 393+10, 40, 403+10), fill=colors_name[0])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: change_width(10))
    id = colors.create_rectangle(
        (start_x, 411+10, 40, 426+10), fill=colors_name[0])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: change_width(15))
    id = colors.create_rectangle(
        (start_x, 434+10, 40, 454+10), fill=colors_name[0])
    colors.tag_bind(id, "<Button-1>",
                    lambda x: change_width(20))


display_pallete()


canvas = Canvas(root, width=19*window_width//20,
                height=window_height, bg="white", cursor="hand2", highlightthickness=0)
canvas.grid(row=0, column=1)

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addLine)


btn_cpicker = Button(root, image=cpicker, width=30-2, height=30, bd=0, bg="#ffffff",
                     highlightthickness=0, highlightbackground="#ffffff", command=choose_color, activebackground='#ffffff')
btn_cpicker.place(
    x=10, y=10)

btn_save = Button(root, image=save, width=30-2, height=30, bd=0, bg="#ffffff",
                  highlightthickness=0, highlightbackground="#ffffff", command=lambda: save_as_png(canvas), activebackground='#ffffff')
btn_save.place(
    x=10, y=window_height-40*3)

btn_eraser = Button(root, image=eraser, width=30-2, height=30, bd=0, bg="#ffffff",
                    highlightthickness=0, highlightbackground="#ffffff", command=lambda: canvas.delete("all"), activebackground='#ffffff')
btn_eraser.place(
    x=10, y=window_height-40*2)


github_url = "https://github.com/aadilmughal786"
btn_github = Button(root, image=github, width=30-2, height=30, bd=0, bg="#ffffff", activebackground='#ffffff',
                    command=lambda: webbrowser.open(github_url), highlightthickness=0, highlightbackground="#ffffff")
btn_github.place(
    x=10, y=window_height-40*1)


root.mainloop()
