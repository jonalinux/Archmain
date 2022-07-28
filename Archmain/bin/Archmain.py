#!/usr/bin/env python
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import os



window=tk.Tk()
window.title('Archmain')
window.geometry("800x600+10+20")
window.maxsize(800, 600)
window.configure(bg='#444')

#top #archcolor #0f94d2
image = PhotoImage(file="./icon/logo.png")
banner = tk.Frame(master=window, height=80, bg="#333")
banner.pack(fill=tk.X)
linebanner = tk.Frame(master=window, height=5, bg="#0f94d2")
linebanner.pack(fill=tk.X)
canvas = Canvas(width = 90, height = 80, bg="#333", borderwidth = 0, highlightthickness = 0)
canvas.create_image(50, 40, image = image)
canvas.place(x=0, y=0)
title = tk.Label(master=window, text="Archmain", font=('Poppins', 25,), bg="#333", fg="#fff")
title.place(x=95, y=12)
subtitle = tk.Label(master=window, text="AUR and Pacman Updater", font=('Poppins',10), bg="#333", fg="#0f94d2")
subtitle.place(x=95, y=50)
info = tk.Label(master=window, text="version 2.0", font=('Poppins',8), bg="#333", fg="#fff")
info.place(x=720, y=50)


#updates list
content = open("./data/listaupds", "r")
    
lista=Text(master=window, font=('Poppins',10), bg='#444', fg="#fff", borderwidth = 0, highlightthickness = 0)
lista.place(x=40, y=100)

for updates in content:
   lista.insert(END, updates + '\n')
lista.config(state=DISABLED)



#find pkgs
def getTextInput():
    result=textExample.get("1.0","end")
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); echo "' + result + '" > $HOME/.local/share/Archmain/data/input' + " ; " + " $TERMINAL -e $HOME/.local/share/Archmain/bin/find.sh")
    
textExample=tk.Text(window, height=1, width=30, bg="#fff", fg='#222', font=('Cantarell bold',15))
textExample.pack(side=tk.BOTTOM)

btnRead=tk.Button(window,  height=1, width=10, text="Find", bg="#303134", fg='#13beaa', font='20px', command=getTextInput)
btnRead.pack(side=tk.BOTTOM)

window.mainloop()





#frame1 = tk.Frame(master=window, height=30, bg="blue")
#frame1.pack(fill=tk.X)
#img = PhotoImage(file='~/.local/share/Archmain/bin/img/logo.png')

