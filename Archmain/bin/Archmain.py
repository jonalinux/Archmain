#!/usr/bin/python
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

from tkinter import *
import tkinter as tk
import os
import getpass
import webbrowser


window=tk.Tk()
window.title('Archmain')
window.geometry("800x600+10+20")
window.maxsize(850, 520)
window.minsize(850, 520)
window.configure(bg='#f6f9fc')
username = getpass.getuser()



#top #archcolor #0f94d2
image = tk.PhotoImage(file="/home/" + username + "/.local/share/Archmain/img/logo.png")
banner = tk.Frame(master=window, height=80, bg="#333")
banner.pack(fill=tk.X)
linebanner = tk.Frame(master=window, height=5, bg="#0f94d2")
linebanner.pack(fill=tk.X)
canvas = Canvas(width = 90, height = 80, bg="#333", borderwidth = 0, highlightthickness = 0)
canvas.create_image(50, 40, image = image)
canvas.place(x=0, y=0)
title = tk.Label(master=window, text="Archmain", font=('Cantarell', 25, 'bold'), bg="#333", fg="#fff")
title.place(x=95, y=12)
subtitle = tk.Label(master=window, text="AUR and Pacman Updater", font=('Cantarell',10), bg="#333", fg="#0f94d2")
subtitle.place(x=95, y=50)
footer = tk.Frame(master=window, width=850, height=30, bg="#ecf2f5", highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
footer.place(x=0, y=490)
version = tk.Label(master=window, text="Version 2.0b", font=('Cantarell',8), bg="#ecf2f5", fg="#666")
version.place(x=775, y=495)
author = tk.Label(master=window, text="© 2022 Jonathan Sanfilippo", font=('Cantarell',8), bg="#ecf2f5", fg="#666")
author.place(x=10, y=495)

def callback(url):
   webbrowser.open_new_tab(url)
   
link = Label(window, text="GitHub",font=('Cantarell', 10,'bold'), bg="#ecf2f5", fg="#0f94d2")
link.place(x=150, y=493)
link.bind("<Button-1>", lambda e:
callback("https://github.com/JonathanSanfilippo/Archmain"))

#-------------------------------------------------------------------------------------------------------------------------





#Package Search:
def package_search():
    result=form.get("1.0",END) #INPUT=$(cat "$HOME/.local/share/Archmain/data/input") pikaur -S $INPUT
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL -e "/usr/bin/pikaur -S "' + result)

background_form = tk.Frame(master=window, width=380, height=45, bg="#0f94d2")
background_form.place(x=430, y=0) 
form=tk.Text(window, height=1, width=20, bg="#fff", fg='#222', font=('Cantarell',12), )
form.place(x=550, y=10)
form_title = tk.Label(master=window, text="Package Install:", font=('Cantarell',10), bg="#0f94d2", fg="#fff")
form_title.place(x=440, y=12)
btnPkgs=tk.Button(window,  height=1, width=3, text="Search", bg="#0f94d2", fg='#fff', font=('Cantarell',10), borderwidth = 0, highlightthickness = 0, command=package_search)
btnPkgs.place(x=755, y=10)

#-------------------------------------------------------------------------------------------------------------------------




#updates list 
background_lista = tk.Frame(master=window, width=528, height=320, bg="#ecf2f5")
background_lista.place(x=30, y=100,)
background_lista.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
content = open(file="/home/" + username + "/.local/share/Archmain/data/listupdates")
#scrollbar = Scrollbar(window)   
lista=Text(master=window,  width=63, height=15,font=('Cantarell',10), bg='#ecf2f5', fg="#555", borderwidth = 0, highlightthickness = 0, )#yscrollcommand=scrollbar.set
#scrollbar.config(command=lista.yview, bg="#0f94d2" , troughcolor="#333")
#scrollbar.pack(side=RIGHT, fill=Y)
lista.place(x=40, y=120,)

for updates in content:
   lista.insert(END, updates )
lista.config(state=DISABLED)

#-------------------------------------------------------------------------------------------------------------------------






# bottom install updates
def install_Updates():
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL -e "/usr/bin/pikaur -Syu"')
    
btnInstall=tk.Button(window, height=1, width=5, text="Install", font=('Cantarell',10, "bold"), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=install_Updates)
btnInstall.place(x=30, y=430,)

lastcheck = open(file="/home/" + username + "/.local/share/Archmain/data/lastcheck")
lastcheck_label_title = tk.Label(master=window, text="Last Check:", font=('Cantarell',10), bg="#f6f9fc", fg="#555")
lastcheck_label_title.place(x=105, y=433)
lastcheck_label = Text(master=window,  width=90, height=1,font=('Cantarell',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
lastcheck_label.place(x=180, y=434)

for info_lastcheck in lastcheck:
   lastcheck_label.insert(END, info_lastcheck )
lastcheck_label.config(state=DISABLED)


#pending-updates
pending = open(file="/home/" + username + "/.local/share/Archmain/data/pending")
pending_label_title = tk.Label(master=window, text="Status:", font=('Cantarell',10), bg="#f6f9fc", fg="#555")
pending_label_title.place(x=360, y=433)
pending_label = Text(master=window,  width=90, height=1,font=('Cantarell',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
pending_label.place(x=410, y=434)

for info_pending in pending:
   pending_label.insert(END, info_pending )
pending_label.config(state=DISABLED)

#-------------------------------------------------------------------------------------------------------------------------





#System info Sidebar
system_info = tk.Label(master=window, text="General System Info", font=('Cantarell',12, 'bold'), bg="#f6f9fc", fg="#555")
system_info.place(x=608, y=93)


pkgs_count = open(file="/home/" + username + "/.local/share/Archmain/data/packages")
pkgs_count_label_title = tk.Label(master=window, text="Packages:", font=('Cantarell',10), bg="#f6f9fc", fg="#555")
pkgs_count_label_title.place(x=600, y=123)
pkgs_count_label = Text(master=window,  width=90, height=1,font=('Cantarell',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
pkgs_count_label.place(x=680, y=125)

for info_pkgs_count in pkgs_count:
   pkgs_count_label.insert(END, info_pkgs_count )
pkgs_count_label.config(state=DISABLED)

#-------------------------------------------------------------------------------------------------------------------------




window.mainloop()





