#!/usr/bin/env python
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

from tkinter import *
import tkinter as tk
import os
from turtle import fillcolor



window=tk.Tk()
window.title('Archmain')
window.geometry("800x600+10+20")
window.maxsize(850, 500)
window.minsize(850, 500)
window.configure(bg='#f6f9fc')

#top #archcolor #0f94d2
image = PhotoImage(file="logo.png")
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
info.place(x=725, y=50)



#Package Search:
def getTextInput():
    result=form.get(END)
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); echo "' + result + '" > $HOME/.local/share/Archmain/data/input' + " ; " + " $TERMINAL -e $HOME/.local/share/Archmain/bin/find.sh")


    

background_form = tk.Frame(master=window, width=380, height=45, bg="#0f94d2")
background_form.place(x=430, y=0) 
form=tk.Text(window, height=1, width=20, bg="#fff", fg='#222', font=('Poppins',10), )
form.place(x=550, y=10)
form_title = tk.Label(master=window, text="Package Install:", font=('Poppins',9), bg="#0f94d2", fg="#fff")
form_title.place(x=440, y=12)
btnPkgs=tk.Button(window,  height=1, width=3, text="Search", bg="#0f94d2", fg='#fff', font=('Poppins',9), borderwidth = 0, highlightthickness = 0, command=getTextInput)
btnPkgs.place(x=740, y=10)





#updates list
#ecf2f5
background_lista = tk.Frame(master=window, width=528, height=320, bg="#ecf2f5")
background_lista.place(x=30, y=100,)
background_lista.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")


content = open(file="listaupds")
scrollbar = Scrollbar(window)   
lista=Text(master=window,  width=63, height=15,font=('Poppins',9), bg='#ecf2f5', fg="#555", borderwidth = 0, highlightthickness = 0, yscrollcommand=scrollbar.set)
scrollbar.config(command=lista.yview, bg="#0f94d2" , troughcolor="#333")
scrollbar.pack(side=RIGHT, fill=Y)
lista.place(x=40, y=120,)

for updates in content:
   lista.insert(END, updates )
lista.config(state=DISABLED)

def install_Updates():
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL -e "/usr/bin/pikaur -Syu"')
    
btnInstall=tk.Button(window, height=1, width=5, text="Install", font=('Poppins',9), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=install_Updates)
btnInstall.place(x=30, y=430,)



lastcheck = open(file="info_lastcheck")
lastcheck_label_title = tk.Label(master=window, text="Last Check:", font=('Poppins',9), bg="#f6f9fc", fg="#555")
lastcheck_label_title.place(x=115, y=433)
lastcheck_label = Text(master=window,  width=90, height=1,font=('Poppins',9), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
lastcheck_label.place(x=185, y=434)

for info_lastcheck in lastcheck:
   lastcheck_label.insert(END, info_lastcheck )
lastcheck_label.config(state=DISABLED)

window.mainloop()





#frame1 = tk.Frame(master=window, height=30, bg="blue")
#frame1.pack(fill=tk.X)
#img = PhotoImage(file='~/.local/share/Archmain/bin/img/logo.png')

