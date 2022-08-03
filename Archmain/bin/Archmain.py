#!/usr/bin/python
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



from distutils.cmd import Command
from tkinter import *
import tkinter as tk
import os
import getpass
from tokenize import Number
from turtle import width
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
title = tk.Label(master=window, text="Archmain", font=('SF Pro Display', 25, 'bold'), bg="#333", fg="#fff")
title.place(x=95, y=12)
subtitle = tk.Label(master=window, text="AUR and Pacman Updater", font=('SF Pro Display',10), bg="#333", fg="#0f94d2")
subtitle.place(x=95, y=50)
footer = tk.Frame(master=window, width=850, height=30, bg="#ecf2f5", highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
footer.place(x=0, y=490)
version = tk.Label(master=window, text="Version 2.0b", font=('SF Pro Display',8), bg="#ecf2f5", fg="#666")
version.place(x=775, y=495)
author = tk.Label(master=window, text="© 2022 Jonathan Sanfilippo", font=('SF Pro Display',8), bg="#ecf2f5", fg="#666")
author.place(x=10, y=495)

def callback(url):
   webbrowser.open_new_tab(url)
   
link = Label(window, text="GitHub",font=('SF Pro Display', 10,'bold'), bg="#ecf2f5", fg="#0f94d2")
link.place(x=150, y=494)
link.bind("<Button-1>", lambda e:
callback("https://github.com/JonathanSanfilippo/Archmain"))

#-------------------------------------------------------------------------------------------------------------------------





#Package Search:
def package_search():
    result=form.get("1.0",END) 
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL -e "/usr/bin/pikaur -S "' + result)

background_form = tk.Frame(master=window, width=380, height=45, bg="#0f94d2")
background_form.place(x=430, y=0) 
form=tk.Text(window, height=1, width=20, bg="#fff", fg='#222', font=('SF Pro Display',12), )
form.place(x=550, y=10)
form_title = tk.Label(master=window, text="Package Install:", font=('SF Pro Display',10), bg="#0f94d2", fg="#fff")
form_title.place(x=440, y=12)
btnPkgs=tk.Button(window,  height=1, width=3, text="Search", bg="#0f94d2", fg='#fff', font=('SF Pro Display',10), borderwidth = 0, highlightthickness = 0, command=package_search)
btnPkgs.place(x=755, y=10)

#-------------------------------------------------------------------------------------------------------------------------




#updates list 
background_lista = tk.Frame(master=window, width=528, height=320, bg="#ecf2f5")
background_lista.place(x=30, y=100,)
background_lista.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
content = open(file="/home/" + username + "/.local/share/Archmain/data/listupdates")
#scrollbar = Scrollbar(window)   
lista=Text(master=window,  width=63, height=15,font=('SF Pro Display',10), bg='#ecf2f5', fg="#555", borderwidth = 0, highlightthickness = 0, )#yscrollcommand=scrollbar.set
#scrollbar.config(command=lista.yview, bg="#0f94d2" , troughcolor="#333")
#scrollbar.pack(side=RIGHT, fill=Y)
lista.place(x=40, y=120,)

for updates in content:
   lista.insert(END, updates )
lista.config(state=DISABLED)

#-------------------------------------------------------------------------------------------------------------------------






# bottom install updates
def install_Updates():
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL -e "/usr/bin/pikaur -Syu"; exit;')
    
btnInstall=tk.Button(window, height=1, width=5, text="Install", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=install_Updates)
btnInstall.place(x=30, y=430,)

lastcheck = open(file="/home/" + username + "/.local/share/Archmain/data/lastcheck")
lastcheck_label_title = tk.Label(master=window, text="Last Check:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
lastcheck_label_title.place(x=105, y=433)
lastcheck_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
lastcheck_label.place(x=180, y=434)

for info_lastcheck in lastcheck:
   lastcheck_label.insert(END, info_lastcheck )
lastcheck_label.config(state=DISABLED)


#pending-updates
pending = open(file="/home/" + username + "/.local/share/Archmain/data/pending")
pending_label_title = tk.Label(master=window, text="Status:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
pending_label_title.place(x=390, y=433)
pending_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
pending_label.place(x=435, y=434)

for info_pending in pending:
   pending_label.insert(END, info_pending )
pending_label.config(state=DISABLED)

#-------------------------------------------------------------------------------------------------------------------------





#System info Sidebar
system_info = tk.Label(master=window, text="System Info", font=('SF Pro Display',10, 'bold'), bg="#f6f9fc", fg="#555")
system_info.place(x=660, y=103)


kernel = open(file="/home/" + username + "/.local/share/Archmain/data/kernel")
kernel_label_title = tk.Label(master=window, text="kernel:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
kernel_label_title.place(x=580, y=133)
kernel_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
kernel_label.place(x=627, y=135)

for info_kernel in kernel:
   kernel_label.insert(END, info_kernel )
kernel_label.config(state=DISABLED)

pkgs_count = open(file="/home/" + username + "/.local/share/Archmain/data/packages")
pkgs_count_label_title = tk.Label(master=window, text="Packages:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
pkgs_count_label_title.place(x=580, y=153)
pkgs_count_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
pkgs_count_label.place(x=645, y=155)

for info_pkgs_count in pkgs_count:
   pkgs_count_label.insert(END, info_pkgs_count )
pkgs_count_label.config(state=DISABLED)

ram = open(file="/home/" + username + "/.local/share/Archmain/data/ram")
ram_label_title = tk.Label(master=window, text="Memory usage:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
ram_label_title.place(x=580, y=173)
ram_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
ram_label.place(x=675, y=175)

for info_ram in ram:
   ram_label.insert(END, info_ram )
   ram_label.config(state=DISABLED)

ssd = open(file="/home/" + username + "/.local/share/Archmain/data/ssd")
ssd_label_title = tk.Label(master=window, text="Disc usage:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
ssd_label_title.place(x=580, y=193)
ssd_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
ssd_label.place(x=650, y=195)

for info_ssd in ssd:
   ssd_label.insert(END, info_ssd )
ssd_label.config(state=DISABLED)

cache = open(file="/home/" + username + "/.local/share/Archmain/data/cache")
cache_label_title = tk.Label(master=window, text="Cache:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
cache_label_title.place(x=580, y=213)
cache_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
cache_label.place(x=626, y=215)

for info_cache in cache:
   cache_label.insert(END, info_cache )
cache_label.config(state=DISABLED)

orphans = open(file="/home/" + username + "/.local/share/Archmain/data/orphans")
orphans_label_title = tk.Label(master=window, text="Unused (orphans):", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
orphans_label_title.place(x=580, y=233)
orphans_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
orphans_label.place(x=690, y=235)

for info_orphans in orphans:
   orphans_label.insert(END, info_orphans )
orphans_label.config(state=DISABLED)


#settings
Settings = tk.Label(master=window, text="Settings", font=('SF Pro Display',10, 'bold'), bg="#f6f9fc", fg="#555")
Settings.place(x=660, y=273)





#Package Search:
def delay_set():
    result=delay_label.get("1.0",END) 
    os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/delay;")
  
delay=open(file="/home/" + username + "/.local/share/Archmain/data/delay")    
conferm="  ok, reboot!"   
delay_label_title = tk.Label(master=window, text="New:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
delay_label_title.place(x=580, y=322)
delay_label = Text(master=window,  height=1, width=15,font=('SF Pro Display',10), bg="#ecf2f5", fg="green", borderwidth = 0, highlightthickness = 0, )
delay_label.place(x=620, y=322)
delay_label.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")

btnSet=tk.Button(window,  height=1, width=3, text="Set", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=lambda:[delay_set(), conferm_set()])
btnSet.place(x=750, y=320)

def conferm_set():
 for x in conferm:
   delay_label.insert(END, x)
   

delay_c=open(file="/home/" + username + "/.local/share/Archmain/data/delay")   
delay_current_title = tk.Label(master=window, text="Current Delay: min", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
delay_current_title.place(x=580, y=298)
delay_current = Text(master=window,  height=1, width=4,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
delay_current.place(x=690, y=300)

for c in delay_c:
    delay_current.insert(END, c)
    delay_current.config(state=DISABLED)
   


#-------------------------------------------------------------------------------------------------------------------------


window.mainloop()





