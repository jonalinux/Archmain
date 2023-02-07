#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Jonathan Sanfilippo
# Program: Archmain - Arch System Management
# Date: Feb 1 2023 - Birmingham, United Kingdom. 
# Copyright (C) 2023 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>
#
#Licenses:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import tkinter as tk
from PIL import Image, ImageTk
import os
import getpass
from tkinter import *
from PIL import Image

app = tk.Tk() 
app.withdraw()

#user
username = getpass.getuser()

def show_splash_screen():
    splash = tk.Toplevel()
    splash.attributes("-topmost", True)
    splash.geometry("600x350+600+350")
    splash.config(bg='#3a5a80')
    splash.overrideredirect(True)

    image = Image.open("/home/" + username + "/.config/archmain/img/repository-open-graph-template.png")
    image = image.resize((600, 300))
    image = ImageTk.PhotoImage(image)
    label_image = tk.Label(splash, image=image, borderwidth=0)
    label_image.image = image
    label_image.pack()
    
    label_loading = tk.Label(splash, text="Starting..", font=("Cantarell bold", 12),fg="white", bg="#3a5a80")
    label_loading.pack(side='left', padx=20, pady=10)
    label_loading.lift()

    vr = os.popen('cat "/home/' + username + '/.config/archmain/version"').read()
    text = "v" + vr
    label_v = tk.Label(splash, text=text, font=("Cantarell bold", 10),fg="white", bg="#3a5a80")
    label_v.pack(side='right', padx=20, pady=0)
    label_v.lift()
    
    splash.after(5000, splash.destroy)
   
    
 
    



show_splash_screen()
app.mainloop()

