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

 

import threading
import tkinter 
import platform
import customtkinter
import os
import subprocess
import getpass
import tkinter as tk
import psutil
from tkinter import *
from PIL import Image
import json
import shutil
import time
from tkinter import Scrollbar
import socket

#info
username = getpass.getuser()
hostname = socket.gethostname()

#app-(app)-Archmain v3.00
app = customtkinter.CTk(className='Archmain') 
app.geometry(f"{1500}x{850}")
app.minsize(1500, 850)
app.maxsize(1500, 850)
app.configure(fg_color=("#f6f8fc","#1f1f1f"))




filename = "/home/" + username + "/.config/archmain/data/n.json"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        pass
           

def title_status():
    app.status = ""
    with open("/home/" + username + "/.config/archmain/data/n.json", "r") as file: n = file.read()
    if n != app.status:
       app.title(f"{n} - {username}@{hostname}")
       app.status = n
    app.after(1000, title_status)
app.title(f"Archmain - Arch System Management")  
app.after(1000, title_status)


filename = "/home/" + username + "/.config/archmain/data/checkSet.json"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("60")
else:
    with open(filename, "r") as f:
        content = f.read()
        if content == "":
            with open(filename, "w") as f:
                f.write("60")
             
filename = "/home/" + username + "/.config/archmain/data/delay.json"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("120")
else:
    with open(filename, "r") as f:
        content = f.read()
        if content == "":
            with open(filename, "w") as f:
                f.write("120")   
                
src = "/home/" + username + "/.config/archmain/data/temp.json"
dst = "/home/" + username + "/.config/archmain/data/last.json"
if not os.path.exists(dst):
    with open(src, "r") as fsrc:
        content = fsrc.read()
        with open(dst, "w") as fdst:
            fdst.write(content)

filename = "/home/" + username + "/.config/archmain/config/country.json"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write('{"country": "gb"}')
else:
    with open(filename, "r") as f:
        content = f.read()
        if content == "":
            with open(filename, "w") as f:
                f.write('{"country": "gb"}')                
    
#icons
icon = tkinter.PhotoImage(file="/home/" + username + "/.config/archmain/icons/app-icon.png")
app.iconphoto(False, icon)   


# Definire il percorso del file JSON 
file_path = "/home/" + username + "/.config/archmain/config/mode.json"

# Impostare il valore predefinito del modo di apparizione e del tema di colore
appearance_mode = "System"
color_theme = customtkinter.set_default_color_theme( "/home/" + username + "/.config/archmain/config/theme.json")

# Provare a caricare la scelta dell'utente dal file JSON
try:
    with open(file_path, "r") as file:
        choice = json.loads(file.read())
        appearance_mode = choice.get("appearance_mode", appearance_mode)
        color_theme = choice.get("color_theme", color_theme)
except FileNotFoundError:
    pass

# Impostare il modo di apparizione e il tema di colore
customtkinter.set_appearance_mode(appearance_mode)
#customtkinter.set_default_color_theme(color_theme)

appearance_mode_var = tkinter.StringVar(value=appearance_mode)
app.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(app,width=90, height=20, dropdown_hover_color=("#3b8ed0","#06c"), values=["Light", "Dark", "System"],
                                                              variable=appearance_mode_var,
                                                              command=lambda value: change_appearance_mode_event(value))
app.appearance_mode_optionemenu.place(x=30, y=815)

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
    with open(file_path, "w") as file:
        choice = {"appearance_mode": new_appearance_mode, "color_theme": color_theme}
        json.dump(choice, file)

label = customtkinter.CTkLabel(master=app,text="Themes", width=50, height=15, )
label.place(x=125, y=817)



#splash-setting
def switch_event():
    switch_value = switch_var.get()
    print("switch toggled, current value:", switch_value)
    data = {}
    data["switch_value"] = switch_value
    with open("/home/" + username + "/.config/archmain/config/splash.json", "w") as file:
        json.dump(data, file)

# Caricare i dati dal file JSON all'avvio dell'app
try:
    with open("/home/" + username + "/.config/archmain/config/splash.json", "r") as file:
        data = json.load(file)
        switch_value = data["switch_value"]
except FileNotFoundError:
    switch_value = "on"

switch_var = customtkinter.StringVar(value=switch_value)
switch_1 = customtkinter.CTkSwitch(master=app, text="Login Splash", command=switch_event,
                                   variable=switch_var, onvalue="on", offvalue="off")
switch_1.place(x=1350, y=815)



#banner-line
linebanner = customtkinter.CTkFrame(master=app, width=1500 ,height=5, fg_color=("#0f94d2","#08c"))
linebanner.place(x=0, y=50)
linebanner = tk.Frame(master=app, width=1500 ,height=50, bg="#333")
linebanner.place(x=0, y=0)

logo = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/img/logo.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/logo.png"),
                                  size=(250, 40))

label003 = customtkinter.CTkLabel(app, image=logo, text=" ", fg_color="#333") #fg_color=('#ecf1f6','#2b2b2b')
label003.place(x=25, y=5)

#label = customtkinter.CTkLabel(app, text="Archmain", font=('Cantarell',24), fg_color="#333", text_color="#FFF")
#label.configure()
#label.place(x=80, y=10)



#terminals
with open('/home/' + username + '/.config/archmain/config/terminals.json', 'r') as file:
    terminals_dict = json.load(file)
 
# Accedi alla lista di terminali
terminals = terminals_dict['terminals']



# Sidebar
app.sidebar_frame = customtkinter.CTkFrame(app, width=170, height=695, corner_radius=12, fg_color=("#ecf1f6","#2b2b2b"), border_color=("#bcd","#333"), border_width=1)
app.sidebar_frame.place(x=20, y=80)

# panel right
app.panel_frame = customtkinter.CTkFrame(app, width=170, height=695, corner_radius=12,fg_color=("#ecf1f6","#2b2b2b"), border_color=("#bcd","#333"), border_width=1)
app.panel_frame.place(x=1310, y=80)



#license
label = customtkinter.CTkLabel(master=app,text="Copyright (C) 2023 Jonathan Sanfilippo - Licensed GPLv3", width=250, height=15, text_color="#868686")
label.place(x=595, y=820)





vr = os.popen('head -n 1 "/home/' + username + '/.config/archmain/version"').read().strip()
text = "v" + vr

# Create the label with the text from the file
app.label = customtkinter.CTkLabel(app, text=text, width=0, height=10, fg_color="#333", text_color="#FFF")
app.label.place(x=1460, y=30)








class MyTabView(customtkinter.CTkTabview):
    def __init__(app, master, **kwargs):
        super().__init__(master, **kwargs)
         
        filename = "/home/" + username + "/.config/archmain/data/processes.json"
        if not os.path.exists(filename):
               with open(filename, "w") as f:
                    pass 
        
        
        filename = "/home/" + username + "/.config/archmain/data/processes.json"
        with open(filename) as f:
                 num_lines = sum(1 for line in f)
           
        
        # create tabs
        app.add(" Console ")
        app.add(f" Processes ({num_lines})")
        app.add(" Updates log ")
        app.add(" Mirrorlist ")
        app.add(" Syslog ")
        app.add(" journalctl ")
        app.add(" Pacman ")
        app.add(" AUR ")
        
        
        # Console
        app.text = ""
        def update_textbox():
            filename = "/home/" + username + "/.config/archmain/data/console.json"
            if not os.path.exists(filename):
               with open(filename, "w") as f:
                    pass
            global textbox
            with open("/home/" + username + "/.config/archmain/data/console.json", "r") as file:
                 new_text = file.read()
            if new_text != app.text:
               textbox.configure(state="normal")  # configure textbox to be editable
               textbox.delete("0.0", "end")  # clear textbox
               textbox.insert("0.0", new_text)  # insert updated text
               textbox.configure(state="disabled")  # configure textbox to be read-only
               app.text = new_text
            app.after(1000, update_textbox)
        
        global textbox
        textbox = customtkinter.CTkTextbox(master=app.tab(" Console "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox.place(x=0, y=0)
        textbox.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox)



        
        def write_processes_to_file():
            # Recupera la lista dei processi in esecuzione
            processes = list(psutil.process_iter())
            # Ordina i processi in base al consumo di CPU
            processes.sort(key=lambda process: process.memory_percent(), reverse=True)
            # Apri il file in modalità di scrittura
            with open("/home/" + username + "/.config/archmain/data/processes.json", "w") as file:
            # Per ogni processo in esecuzione
               for process in processes:
                try:
                   # Recupera informazioni sul processo
                   process_info = process.as_dict(attrs=["pid", "name", "status"])
                   # Recupera informazioni sul consumo di CPU e RAM del processo
                   cpu_percent = process.cpu_percent()
                   memory_info = process.memory_info().rss / 1024 / 1024
                   # Scrivi le informazioni sul processo nel file
                   file.write(f"{process_info['name']} {process_info['pid']}: - CPU: {cpu_percent}%, RAM: {memory_info:.2f} MB\n")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                   pass
            app.after(10000,write_processes_to_file)      
        
        app.after(1000,write_processes_to_file)        
        
         # Processes
        app.text2 = ""
        def update_textbox2():
            global textbox2
            with open("/home/" + username + "/.config/archmain/data/processes.json", "r") as file:
                 new_text = file.read()
            if new_text != app.text2:
               textbox2.configure(state="normal")  # configure textbox to be editable
               textbox2.delete("0.0", "end")  # clear textbox
               textbox2.insert("0.0", new_text)  # insert updated text
               textbox2.configure(state="disabled")  # configure textbox to be read-only
               app.text2 = new_text
            app.after(1000, update_textbox2)
        
        global textbox2
        textbox2 = customtkinter.CTkTextbox(master=app.tab(f" Processes ({num_lines})"), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox2.place(x=0, y=0)
        textbox2.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox2)  
            
            
        
        app.text3 = ""
        def update_textbox3():
            global textbox3
            with open("/home/" + username + "/.config/archmain/data/last.json", "r") as file:
                 new_text = file.read()
            if new_text != app.text3:
               textbox3.configure(state="normal")  # configure textbox to be editable
               textbox3.delete("0.0", "end")  # clear textbox
               textbox3.insert("0.0", new_text)  # insert updated text
               textbox3.configure(state="disabled")  # configure textbox to be read-only
               app.text3 = new_text
            app.after(1000, update_textbox3)
        
        global textbox3
        textbox3 = customtkinter.CTkTextbox(master=app.tab(" Updates log "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox3.place(x=0, y=0)
        textbox3.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox3)      


        #Mirrorslist-tab
        app.text4 = ""
        def update_textbox4():
            global textbox4
            with open("/etc/pacman.d/mirrorlist", "r") as file:
                    lines = file.readlines()
                    new_text = ''.join([line.replace("Server = ","") for line in lines[10:]])
            if new_text != app.text4:
               textbox4.configure(state="normal")  # configure textbox to be editable
               textbox4.delete("0.0", "end")  # clear textbox
               textbox4.insert("0.0", new_text)  # insert updated text
               textbox4.configure(state="disabled")  # configure textbox to be read-only
               app.text4 = new_text
            app.after(1000, update_textbox4)
        
        global textbox4
        textbox4 = customtkinter.CTkTextbox(master=app.tab(" Mirrorlist "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox4.place(x=0, y=0)
        textbox4.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox4)      
        
        
        
        
        
        app.text5 = ""
        #syslog
        def perm_syslog():
             terminal = None
             for t in terminals:
                if os.system(f"which {t}") == 0:
                   terminal = t
                   break
        
             if terminal:
                subprocess.call([terminal, "-e","sudo chmod +r /var/log/syslog.log"])
             with open("/var/log/syslog.log", "r") as file:
                    lines = file.readlines()
                    new_text = ''.join(reversed(lines[0:]))
             if new_text != app.text5:
                textbox5 = customtkinter.CTkTextbox(master=app.tab(" Syslog "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
                textbox5.place(x=0, y=0)
                textbox5.configure(state="normal")  # configure textbox to be editable
                textbox5.delete("0.0", "end")  # clear textbox
                textbox5.insert("0.0", new_text)  # insert updated text
                textbox5.configure(state="disabled")  # configure textbox to be read-only
                app.text5 = new_text
             else:
                textbox5.configure(state="normal")  # configure textbox to be editable
                textbox5.delete("0.0", "end")  # clear textbox
                textbox5.insert("0.0", new_text)  # insert updated text
                textbox5.configure(state="disabled")  # configure textbox to be read-only
            
        def but_syslog():
             label = customtkinter.CTkLabel(master=app.tab(" Syslog "), text="Need permission to enable reading of file '/var/log/syslog.log'")
             label.place(x=10, y=10) 
             button = customtkinter.CTkButton(master=app.tab(" Syslog "), width=90, text="enable",text_color=("gray10", "#DCE4EE"), fg_color=("#ccc","#333"),hover_color=("limegreen","limegreen"),command=perm_syslog)
             button.place(x=400, y=12) 
        but_syslog()
        
        
        #jctl
        app.text6 = ""
        def update_textbox6():
            global textbox6
            os.system("journalctl -p 3 -b -n > /home/" + username + "/.config/archmain/data/jctl.json")
            with open("/home/" + username + "/.config/archmain/data/jctl.json", "r") as file:
                 new_text = file.read()
            if new_text != app.text6:
               textbox6.configure(state="normal")  # configure textbox to be editable
               textbox6.delete("0.0", "end")  # clear textbox
               textbox6.insert("0.0", new_text)  # insert updated text
               textbox6.configure(state="disabled")  # configure textbox to be read-only
               app.text6 = new_text
            app.after(1000, update_textbox6)
        
        global textbox6
        textbox6 = customtkinter.CTkTextbox(master=app.tab(" journalctl "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox6.place(x=0, y=0)
        textbox6.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox6)  
 
         #pkgs-pacman
        app.text7 = ""
        def update_textbox7():
            global textbox7
            os.system("  pikaur -Q > /home/" + username + "/.config/archmain/data/pkgs-pacman.json")
            with open("/home/" + username + "/.config/archmain/data/pkgs-pacman.json", "r") as file:
                 new_text = file.read()
            if new_text != app.text7:
               textbox7.configure(state="normal")  # configure textbox to be editable
               textbox7.delete("0.0", "end")  # clear textbox
               textbox7.insert("0.0", new_text)  # insert updated text
               textbox7.configure(state="disabled")  # configure textbox to be read-only
               app.text7 = new_text
            app.after(1000, update_textbox7)
        
        global textbox7
        textbox7 = customtkinter.CTkTextbox(master=app.tab(" Pacman "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox7.place(x=0, y=0)
        textbox7.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox7)  

         #pkgs-aur
        app.text8 = ""
        def update_textbox8():
            global textbox8
            os.system("  pikaur -Qm > /home/" + username + "/.config/archmain/data/pkgs-aur.json")
            with open("/home/" + username + "/.config/archmain/data/pkgs-aur.json", "r") as file:
                 new_text = file.read()
            if new_text != app.text8:
               textbox8.configure(state="normal")  # configure textbox to be editable
               textbox8.delete("0.0", "end")  # clear textbox
               textbox8.insert("0.0", new_text)  # insert updated text
               textbox8.configure(state="disabled")  # configure textbox to be read-only
               app.text8 = new_text
            app.after(1000, update_textbox8)
        
        global textbox8
        textbox8 = customtkinter.CTkTextbox(master=app.tab(" AUR "), width=1084, height=348, font=('source code pro',14),border_color=("#bcd","#2b2b2b"), border_width=1)
        textbox8.place(x=0, y=0)
        textbox8.configure(state="disabled") # configure textbox to be read-only
        app.after(1000, update_textbox8)  



app.tab_view = MyTabView(master=app, width=1096, height=395,fg_color=("#ecf1f6","#2b2b2b"), border_color=("#bcd","#333"), border_width=1)
app.tab_view.place(x=203, y=65)

#------------------------------------------------------------------------------------------------ end tab


      
        


#Update Now
def check_updates():
    terminal = None
    for t in terminals:
        if os.system(f"which {t}") == 0:
            terminal = t
            break

    if terminal:
        subprocess.call([terminal, "-e", "/home/" + username + "/.config/archmain/scripts/updatenow"])
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    else:
        print("No supported terminal found.")

def start_progress_bar_check():
    progressbar.place(x=625, y=480)
    progressbar.start()
    thread = threading.Thread(target=check_updates)
    thread.start()        
        
def button_function(): 
    print("button pressed")




button = customtkinter.CTkButton(app, border_color="#0f94d2",  text_color=("#DCE4EE", "#DCE4EE"), border_width=0, corner_radius=4, text=f"Update Now", command=start_progress_bar_check)
button.place(x=35, y=86)





#ignore-AUR
def ignore_AUR():
    terminal = None
    for t in terminals:
        if os.system(f"which {t}") == 0:
            terminal = t
            break

    if terminal:
        subprocess.call([terminal, "-e", "/home/" + username + "/.config/archmain/scripts/ignore-AUR"])
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    else:
        print("No supported terminal found.")

def start_progress_bar_ign():
    progressbar.place(x=625, y=480)
    progressbar.start()
    thread = threading.Thread(target=ignore_AUR)
    thread.start()            
        
def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, border_color="#0f94d2", fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), border_width=0, corner_radius=4, text="Ignore AUR", command=start_progress_bar_ign)
button.place(x=35, y=120)



#manual-Check
def man_check_updates():
    subprocess.call(["bash", "/home/" + username + "/.config/archmain/scripts/verified"])
    progressbar.stop()
    app.after(1000, lambda: progressbar.place_forget())

def start_progress_bar_man():
    progressbar.place(x=625, y=480)
    progressbar.start()
    thread = threading.Thread(target=man_check_updates)
    thread.start()

button = customtkinter.CTkButton(master=app,
                                 border_color="#0f94d2",
                                 fg_color=("#ccc","#333"),
                                 text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="Manual Check",
                                 command=start_progress_bar_man)
button.place(x=35, y=152)


#New-mirrors
def load_config_c():
    with open("/home/" + username + "/.config/archmain/config/country.json", 'r') as f:
        country = json.load(f)
        return country["country"]
value_c = load_config_c()






def new_mirrors():
    # get the value selected from the dropdown menu
    country = entry_country.get()
    # save the selected value in an external file named country
    with open("/home/" + username + "/.config/archmain/config/country.json", "w") as f:
      json.dump({"country": country}, f)


    # Loop through each terminal in the list
    for terminal in terminals:
        # Check if the terminal is installed
        if os.system(f"command -v {terminal}") == 0:
            # If the terminal is installed, run the command to update the mirrors
            os.system(f"{terminal} -e ' sudo reflector --verbose --country {country} --sort rate --save /etc/pacman.d/mirrorlist '")
            break
    # Ferma la progressbar
    progressbar.stop()
    # Nascondi la progressbar dopo 1 secondo
    app.after(1000, lambda: progressbar.place_forget())

def start_progress_bar():
    # Mostra la progressbar
    progressbar.place(x=625, y=480)
    # Avvia la progressbar
    progressbar.start()
    # Crea un nuovo thread per eseguire il comando bash
    thread = threading.Thread(target=new_mirrors)
    thread.start()

def change_bg_color_mirr(event=None):
    content = entry_country.get()
    if content.islower():
        entry_country.configure(text_color=("#333","#f2f2f2"))
        
        
button = customtkinter.CTkButton(master=app,width=90,
                                 border_color="#0f94d2",
                                 fg_color=("#ccc","#333"),
                                 text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="New Mirrors",
                                 command=start_progress_bar)
button.place(x=35, y=185)

entry_country = customtkinter.CTkEntry(master=app, width=50,text_color=("#06c","#2997ff"))##3dbeff
entry_country.insert(0, value_c) # imposta il valore iniziale
entry_country.bind("<FocusIn>", change_bg_color_mirr)
entry_country.place(x=128, y=184)


#fstab

def load_config_editor():
    with open("/home/" + username + "/.config/archmain/config/editor.json", 'r') as f:
        editor = json.load(f)
        return editor["editor"]
value_c = load_config_editor()

def fstab():
    # get the value selected from the dropdown menu
    editor = entry_editor.get()
    # save the selected value in an external file named editor
    with open("/home/" + username + "/.config/archmain/config/editor.json", "w") as f:
      json.dump({"editor": editor}, f)


    # Loop through each terminal in the list
    for terminal in terminals:
        # Check if the terminal is installed
        if os.system(f"command -v {terminal}") == 0:
            # If the terminal is installed, run the command to update the mirrors
            os.system(f"{terminal} -e ' sudo {editor} /etc/fstab'")
            break
    # Ferma la progressbar
    progressbar.stop()
    # Nascondi la progressbar dopo 1 secondo
    app.after(1000, lambda: progressbar.place_forget())

def start_progress_bar():
    # Mostra la progressbar
    progressbar.place(x=625, y=480)
    # Avvia la progressbar
    progressbar.start()
    # Crea un nuovo thread per eseguire il comando bash
    thread = threading.Thread(target=fstab)
    thread.start()

def change_bg_color_editor(event=None):
    content = load_config_c()
    if content.islower():
        entry_editor.configure(text_color=("#333","#f2f2f2"))

button = customtkinter.CTkButton(master=app,width=90,
                                 border_color="#0f94d2",
                                 fg_color=("#ccc","#333"),
                                 text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="Edit fstab",
                                 command=start_progress_bar)
button.place(x=35, y=217)

entry_editor = customtkinter.CTkEntry(master=app, width=50,text_color=("#06c","#2997ff"))
entry_editor.insert(0, value_c) # imposta il valore iniziale
entry_editor.bind("<FocusIn>", change_bg_color_editor)
entry_editor.place(x=128, y=217)




def delete_dblck():
    if terminal:
        time.sleep(5)
        os.system("rm /var/lib/pacman/db.lck")
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    after_dblck()
    
def after_dblck():
    if not os.path.exists('/var/lib/pacman/db.lck'):
       with open("/home/" + username + "/.config/archmain/data/console.json", 'w') as f:
            f.write("The db.lck file has been removed or is not present.")        

def start_progress_bar():
    # Mostra la progressbar
    progressbar.place(x=625, y=480)
    # Avvia la progressbar
    progressbar.start()
    # Crea un nuovo thread per eseguire il comando bash
    thread = threading.Thread(target=delete_dblck)
    thread.start()
    
def check_dblck():
    if os.path.exists('/var/lib/pacman/db.lck'):
       with open("/home/" + username + "/.config/archmain/data/console.json", 'w') as f:
            f.write("Warning, the database lock has not been released. To fix the issue, you can use 'remove db.lck\nif you are upgrading or downgrading you can ignore the message.'.")




button = customtkinter.CTkButton(master=app,width=140,
                                 border_color="#0f94d2",
                                 fg_color=("#ccc","#333"),
                                 text_color=("gray10", "#DCE4EE"),hover_color=("#df4848","#df4848"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="Delete db.lck",
                                 command=start_progress_bar)
button.place(x=35, y=250)





#delay
# Carica il valore attuale dal file di configurazione
def load_config():
    with open("/home/" + username + "/.config/archmain/data/delay.json", 'r') as f:
        return f.read()
value = load_config()


# Scrive il nuovo valore nel file di configurazione
def write_config(value):
     with open("/home/" + username + "/.config/archmain/data/delay.json", 'w') as f:
       f.write(value)

# Funzione eseguita quando si seleziona un nuovo valore nel menu a tendina
def optionmenu_callback(choice):
    write_config(choice)

# Crea il menu a tendina
text_var = tkinter.StringVar(value="Delay Min")

label = customtkinter.CTkLabel(master=app,textvariable=text_var,width=0,height=25, fg_color=('#ecf1f6','#2b2b2b'), bg_color=('#ecf1f6','#2b2b2b'))
label.place(x=1405, y=88)

combobox = customtkinter.CTkOptionMenu(master=app,dropdown_hover_color=("#3b8ed0","#06c"),width=70,
                                         values=["120", "180", "240","1440"],
                                         command=optionmenu_callback)
combobox.place(x=1325, y=86)
combobox.set(load_config())  # imposta il valore iniziale


#checkSet
# Carica il valore attuale dal file di configurazione
def load_config_2():
    with open("/home/" + username + "/.config/archmain/data/checkSet.json", 'r') as f:
        return f.read()
value_2 = load_config_2()


# Scrive il nuovo valore nel file di configurazione
def write_config_2(value_2):
     with open("/home/" + username + "/.config/archmain/data/checkSet.json", 'w') as f:
       f.write(value_2)

# Funzione eseguita quando si seleziona un nuovo valore nell'opzione menù
def optionmenu_callback_2(choice):
    value_2 = choice
    write_config_2(value_2)


# Crea l'opzione menù
text_var = tkinter.StringVar(value="Check Min")

label = customtkinter.CTkLabel(master=app,textvariable=text_var, width=0,height=25,fg_color=('#ecf1f6','#2b2b2b'), bg_color=('#ecf1f6','#2b2b2b'))
label.place(x=1405, y=120)

combobox_2 = customtkinter.CTkOptionMenu(master=app,dropdown_hover_color=("#3b8ed0","#06c"), width=70,
                                         values=["60", "120", "180","1440"],
                                         command=optionmenu_callback_2)
combobox_2.place(x=1325, y=118)
combobox_2.set(load_config_2())  # imposta il valore iniziale


#-Ricerca multi-opzioni
def search_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur {entry_value.get()}'")
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    else:
        print("No supported terminal found.")

def install_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur -S {entry_value.get()}'")
        pikaur = subprocess.run(["pikaur", "-V"], capture_output=True, text=True)
        with open("/home/" + username + "/.config/archmain/data/console.json", "w") as file:
         file.write("Hello " + username + "!!\n" + pikaur.stdout) 
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    else:
        print("No supported terminal found.")

def remove_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur -Rns {entry_value.get()}'")
        pikaur = subprocess.run(["pikaur", "-V"], capture_output=True, text=True)
        with open("/home/" + username + "/.config/archmain/data/console.json", "w") as file:
         file.write("Hello " + username + "!!\n" + pikaur.stdout) 
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    else:
        print("No supported terminal found.")

def ignore_package():
    time.sleep(5)
    with open("/home/" + username + "/.config/archmain/data/ignore.json", "a") as f:
        f.write(f"{entry_value.get()}\n")
    progressbar.stop()
    app.after(1000, lambda: progressbar.place_forget())

def downgrade_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo downgrade {entry_value.get()}'")
        subprocess.call(["bash", "/home/" + username + "/.config/archmain/scripts/verified"])
        progressbar.stop()
        app.after(1000, lambda: progressbar.place_forget())
    else:
        print("No supported terminal found.")

terminal = None 
for t in terminals: 
    if os.system(f"which {t}") == 0:
        terminal = t
        break



def clear_entry():
    entry_value.set("")
button = customtkinter.CTkButton(master=app, width=50, text="Del",text_color="#FFF",  fg_color="#555",hover_color=("#df4848","#df4848"), bg_color="#333",command=clear_entry)
button.place(x=450, y=12)    

def change_bg_color(event=None):
    content = entry_value.get()
    if content.islower():
        entry.configure(text_color=("#333","#f2f2f2"))
        

 

entry_value = tk.StringVar()
entry_value.set("before using the options, insert the package name.")
entry = customtkinter.CTkEntry(app, textvariable=entry_value, width=430, height=29, text_color=("#06c","#2997ff"), bg_color="#333")
entry.place(x=503, y=12)
entry.bind("<FocusIn>", change_bg_color)
entry.bind("<KeyRelease>", change_bg_color)


actions = ['Search', 'Install', 'Remove', 'Ignore', 'Downgrade']
combobox_var = customtkinter.StringVar(value="Options")

def combobox_callback(choice):   
    content = entry_value.get()
    if not content.islower():
        entry.configure(text_color=("red","#e8493a"))
        with open("/home/" + username + "/.config/archmain/data/console.json", "w") as file:
            file.write("Warning! The package names in the entry must be written in lowercase!")
            
        return content.islower()
    if choice in ('Search', 'Install', 'Remove', 'Ignore', 'Downgrade'):
        pikaur = subprocess.run(["pikaur", "-V"], capture_output=True, text=True)
        with open("/home/" + username + "/.config/archmain/data/console.json", "w") as file:
         file.write("Hello " + username + "!!\n" + pikaur.stdout)  
        progressbar.place(x=625, y=480)
        progressbar.start()   
        threading.Thread(target=globals()[choice.lower() + '_package'], args=(), daemon=True).start()

   
combobox = customtkinter.CTkComboBox(master=app,width=120, dropdown_hover_color=("#3b8ed0","#06c"), bg_color="#333", values=actions, variable=combobox_var, command=combobox_callback)
combobox.place(x=935, y=12)

def reset():
    with open("/home/" + username + "/.config/archmain/data/ignore.json", "w") as file:
        file.write("")
reset()


#cpu-disk-ram-swap-boot
def update_values():
    disk_usage = psutil.disk_usage("/").percent
    disk_progress.set(value=disk_usage/100)
    disk_label.configure(text="Disk  {:.2f}%".format(disk_usage))

    ram_usage = psutil.virtual_memory().percent
    ram_progress.set(value=ram_usage/100)
    ram_label.configure(text="RAM  {:.2f}%".format(ram_usage))

    swap_usage = psutil.swap_memory().percent
    swap_progress.set(value=swap_usage/100)
    swap_label.configure(text="Swap  {:.2f}%".format(swap_usage))
    
    cpu_usage = psutil.cpu_percent()
    cpu_progress.set(value=cpu_usage/100)
    cpu_label.configure(text="CPU  {:.2f}%".format(cpu_usage))
 
    boot_partition_usage = psutil.disk_usage("/boot").percent
    boot_partition_progress.set(value=boot_partition_usage/100)
    boot_partition_label.configure(text="Boot {:.2f}%".format(boot_partition_usage))

    app.after(1000, update_values)


app.after(1000, update_values)

cpu_label = customtkinter.CTkLabel(app, text="CPU" , fg_color=('#ecf1f6','#2b2b2b'))
cpu_label.place(x=1330, y=237)

cpu_progress = customtkinter.CTkProgressBar(app, height=5, width=130, progress_color="red")
cpu_progress.place(x=1330, y=260)

disk_label = customtkinter.CTkLabel(app, text="Disk ", fg_color=('#ecf1f6','#2b2b2b'))
disk_label.place(x=1330, y=267)

disk_progress = customtkinter.CTkProgressBar(app, height=5, width=130, progress_color="#0f94d2")
disk_progress.place(x=1330, y=290)

ram_label = customtkinter.CTkLabel(app, text="RAM ", fg_color=('#ecf1f6','#2b2b2b'))
ram_label.place(x=1330, y=297)

ram_progress = customtkinter.CTkProgressBar(app, height=5,width=130, progress_color="orange")
ram_progress.place(x=1330, y=320)

swap_label = customtkinter.CTkLabel(app, text="Swap ", fg_color=('#ecf1f6','#2b2b2b'))
swap_label.place(x=1330, y=327)

swap_progress = customtkinter.CTkProgressBar(app, height=5,width=130, progress_color="magenta")
swap_progress.place(x=1330, y=350)

boot_partition_label = customtkinter.CTkLabel(app, text="Boot ", fg_color=('#ecf1f6','#2b2b2b'))
boot_partition_label.place(x=1330, y=357)

boot_partition_progress = customtkinter.CTkProgressBar(app, height=5,width=130, progress_color="#55ff00")
boot_partition_progress.place(x=1330, y=380)

def count_installed_packages():
    output = subprocess.run(['pikaur', '-Q'], stdout=subprocess.PIPE)
    packages = output.stdout.decode('utf-8').split('\n')
    return len(packages)


def update_kernel_info():
    kernel = platform.release()
    kernel_label.configure(text="Kernel: {}".format(kernel))
    kernel_label.after(1000, update_kernel_info)
    
kernel_label = customtkinter.CTkLabel(app, text="Kernel: ...", fg_color=('#ecf1f6','#2b2b2b'))
kernel_label.place(x=1330, y=165)
app.after(1000, update_kernel_info)

def update_mirrorlist_info():
    mirrorlist = subprocess.run(['bash', '-c', 'mirrorlist=$(cat /etc/pacman.d/mirrorlist | wc -l ); diff=$( expr $mirrorlist - 10); echo $diff'], capture_output=True, text=True)
    diff = int(mirrorlist.stdout.strip())
    mirrorlist_label.configure(text="Server Mirrors: {}".format(diff))
    mirrorlist_label.after(1000, update_mirrorlist_info)

mirrorlist_label = customtkinter.CTkLabel(app, text="Server Mirrors: ...", fg_color=('#ecf1f6','#2b2b2b'))
mirrorlist_label.place(x=1330, y=185)
app.after(1000, update_mirrorlist_info)

def update_packages_info():
    packages = count_installed_packages()
    label.configure(text="Packages: {}".format(packages))
    label.after(1000, update_packages_info)

label = customtkinter.CTkLabel(app,fg_color=('#ecf1f6','#2b2b2b'),text="Packages: {}".format(count_installed_packages()))
label.place(x=1330, y=205)
app.after(1000, update_packages_info)


#network
def get_speed():
    net_io_counters = psutil.net_io_counters()
    return (net_io_counters.bytes_sent, net_io_counters.bytes_recv)

def convert_size(size_bytes):
    # Funzione per convertire i byte in megabyte, gigabyte o kilobyte in base alla grandezza
    # del valore
    if size_bytes > 1024 ** 3:
        return "%.2f GB" % (size_bytes / (1024 ** 3))
    elif size_bytes > 1024 ** 2:
        return "%.2f MB" % (size_bytes / (1024 ** 2))
    elif size_bytes > 1024:
        return "%.2f KB" % (size_bytes / 1024)
    else:
        return "%d B" % size_bytes


def convert_speed(speed):
    if speed < 1024:
        return speed, "KB/s"
    elif speed < 1024**2:
        return speed/1024, "MB/s"
    else:
        return speed/(1024**2), "GB/s"


def update_speed_thread():
    while True:
        upload0, download0 = get_speed()
        time.sleep(1)
        upload1, download1 = get_speed()
        upload_speed = (upload1 - upload0) / 1000
        download_speed = (download1 - download0) / 1000
        upload_speed, upload_unit = convert_speed(upload_speed)
        download_speed, download_unit = convert_speed(download_speed)
        upload_speed_label.configure(text="Up: {:.2f} {}".format(upload_speed, upload_unit))
        download_speed_label.configure(text="Down {:.2f} {}".format(download_speed, download_unit))

def update_label_thread():
    while True:
        upload, download = get_speed()
        upload_label.configure(text="Sent: {}".format(convert_size(upload)))
        download_label.configure(text="Received: {}".format(convert_size(download)))
        time.sleep(0.1)

Network_label = customtkinter.CTkLabel(app, text="Network data", fg_color=('#ecf1f6','#2b2b2b'))
Network_label.place(x=1330, y=415)
upload_label = customtkinter.CTkLabel(app, text="Sent...", fg_color=('#ecf1f6','#2b2b2b'), text_color=("#8f2af5","#ba7ff5"))
upload_label.place(x=1330, y=435)
download_label = customtkinter.CTkLabel(app, text="Received...", fg_color=('#ecf1f6','#2b2b2b'), text_color=("#09ba00","#85f57f"))
download_label.place(x=1330, y=455)
Network_label2 = customtkinter.CTkLabel(app, text="Network speed", fg_color=('#ecf1f6','#2b2b2b'))
Network_label2.place(x=1330, y=495)
upload_speed_label = customtkinter.CTkLabel(app, text="Upload... ", fg_color=('#ecf1f6','#2b2b2b'), text_color=("#8f2af5","#ba7ff5"))
upload_speed_label.place(x=1330, y=515)
download_speed_label = customtkinter.CTkLabel(app, text="Download...", fg_color=('#ecf1f6','#2b2b2b'),  text_color=("#09ba00","#85f57f"))
download_speed_label.place(x=1330, y=535)

speed_thread = threading.Thread(target=update_speed_thread, daemon=True)
label_thread = threading.Thread(target=update_label_thread, daemon=True)

speed_thread.start()
label_thread.start()










class SystemCleaner(customtkinter.CTkTabview):
    def __init__(app, master, **kwargs):
        super().__init__(master, **kwargs)
        
        app.add(" System Cleaner ")
        
       
        
        #img "img/001.png"
        pkgs = customtkinter.CTkImage( light_image=Image.open("/home/" + username + "/.config/archmain/img/001.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/001.png"),
                                  size=(40, 40))

        label001 = customtkinter.CTkLabel(master=app.tab(" System Cleaner "), image=pkgs, text=" ")
        label001.place(x=525, y=30)


        home = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/img/002.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/002.png"),
                                  size=(40, 40))

        label002 = customtkinter.CTkLabel(master=app.tab(" System Cleaner "), image=home, text=" ")
        label002.place(x=120, y=30)

        orph = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/img/003.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/003.png"),
                                  size=(40, 40))

        label003 = customtkinter.CTkLabel(master=app.tab(" System Cleaner "), image=orph, text=" ")
        label003.place(x=930, y=30)


                #cache-home-bin
        def get_cache_and_trash_size():
            result = subprocess.check_output(["du", "-sh", "/home/" + username + "/.cache/", "/home/" + username + "/.local/share/Trash/", "/home/" + username ])
            sizes = result.splitlines()
            cache_size = sizes[0].split()[0].decode("utf-8")
            trash_size = sizes[1].split()[0].decode("utf-8")
            home_size_str = sizes[2].split()[0].decode('utf-8')
       
            return cache_size, trash_size, home_size_str

        def clear_cache_and_trash():
            time.sleep(5)
            os.system("rm -rf ~/.cache/*")
            os.system("rm -rf ~/.local/share/Trash/*")
            progressbar.stop()
            app.after(1000, lambda: progressbar.place_forget()) 
            update_info_label()

        def start_progress_bar_cachehome():
            progressbar.place(x=625, y=480)
            progressbar.start()
            thread = threading.Thread(target=clear_cache_and_trash)
            thread.start()
        
        def update_info_label():
            cache_size, trash_size, home_size_str = get_cache_and_trash_size()
            text_var2.set(f"Cache home: {cache_size}B\nTrash: {trash_size}B\nHome: {home_size_str}B")
            app.after(1000, update_info_label)
        
        text_var2 = customtkinter.StringVar(value="Cache size: updating...\nTrash size: updating...")
        
        info_label = customtkinter.CTkLabel(master=app.tab(" System Cleaner "),
                                    textvariable=text_var2,
                                    width=120,
                                    height=40)
        info_label.place(x=80, y=120)
        
        clear_button = customtkinter.CTkButton(master=app.tab(" System Cleaner "), width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Clear", command=start_progress_bar_cachehome)
        clear_button.place(x=100, y=80)
        
        
        update_info_label()
        app.after(1000, update_info_label)



        #Cache-Packages
        def clear_cache_pkg():
            for terminal in terminals:
                try:
                    subprocess.call([terminal, '-e', 'sudo pikaur -Sc'])
                    progressbar.stop()
                    app.after(1000, lambda: progressbar.place_forget()) 
                    break
                except:
                    continue
        
        def start_progress_bar_cachepkgs():
            progressbar.place(x=625, y=480)
            progressbar.start()
            thread = threading.Thread(target=clear_cache_pkg)
            thread.start()  
        
            update_label()
        clean_cache_button = customtkinter.CTkButton(master=app.tab(" System Cleaner "), width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Clear",  command=start_progress_bar_cachepkgs)
        clean_cache_button.place(x=505, y=80)
        
        #mostra valore cache
        def get_cache_size():
            result = subprocess.check_output(["du", "-sh", "/var/cache/pacman/pkg/", "/var/lib/pacman/"])
            sizes = result.splitlines()
            pacman = sizes[0].split()[0].decode("utf-8")
            vlp = sizes[1].split()[0].decode("utf-8")
            return pacman, vlp
        
        
        
        def update_label():
            pacman, vlp = get_cache_size()
            text_var.set("Pacman pkg: " + pacman + "B\n Pacman lib: " + vlp + "B")
            app.after(1000, update_label)
            
        text_var = tkinter.StringVar(value="Cache size: updating...")
        
        label = customtkinter.CTkLabel(master=app.tab(" System Cleaner "),
                                       textvariable=text_var,
                                       width=250,
                                       height=25,
                                       )
        label.place(x=420, y=120)
        
        app.after(1000, update_label)
        
        update_label()
        
        
        
        
        
        #Orphans
        orphan_pkgs_label_text = tkinter.StringVar()
        orphan_pkgs_label_text.set("Orphan Packages: N/A")
        
        
        # Funzione per pulire la cache dei pacchetti orfani
        def clear_orphan_pkgs():
            for terminal in terminals:
                try:
                    if terminal == 'gnome-terminal':
                        subprocess.call([terminal,  '--', "/home/" + username + "/.config/archmain/scripts/remove-orphans"])
                        progressbar.stop()
                        app.after(1000, lambda: progressbar.place_forget()) 
                    else:
                        subprocess.call([terminal, '-e', "/home/" + username + "/.config/archmain/scripts/remove-orphans"])
                        progressbar.stop()
                        app.after(1000, lambda: progressbar.place_forget()) 
                    break
                except:
                    continue
            update_orphan_pkgs_label()
        
        def update_orphan_pkgs_label():
            try:
                output = subprocess.check_output(['pacman', '-Qtdq'], universal_newlines=True)
                num_orphan_pkgs = len(output.splitlines())
                orphan_pkgs_label_text.set(f"Orphan: {num_orphan_pkgs}")
            except:
                orphan_pkgs_label_text.set("No Orphan")
        
        def start_progress_bar_orphans():
            progressbar.place(x=625, y=480)
            progressbar.start()
            thread = threading.Thread(target=clear_orphan_pkgs)
            thread.start()  
        
        # Creazione del bottone per pulire la cache dei pacchetti orfani
        clear_orphan_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Remove", command=start_progress_bar_orphans)
        clear_orphan_button.place(x=915, y=122)
        
        # Creazione della label che mostra il numero di pacchetti orfani
        orphan_pkgs_label = customtkinter.CTkLabel(app, textvariable=orphan_pkgs_label_text, width=120, height=25)
        orphan_pkgs_label.place(x=898, y=155)
        app.after(1000, update_orphan_pkgs_label) 
        
        update_orphan_pkgs_label()
        
        
        def update_orphan_pkgs_label():
            try:
                output = subprocess.check_output(['pacman', '-Qtdq'], universal_newlines=True)
                num_orphan_pkgs = len(output.splitlines())
                orphan_pkgs_label_text.set(f"Orphan: {num_orphan_pkgs}")
            except:
                orphan_pkgs_label_text.set("No Orphan")
            app.after(1000, update_orphan_pkgs_label) 
        
        update_orphan_pkgs_label()
        
        


app.tab_view = SystemCleaner(master=app, width=1096, height=260,fg_color=("#ecf1f6","#2b2b2b"), border_color=("#bcd","#333"), border_width=1)
app.tab_view.place(x=203, y=490)




#group-add-remove

def load_config_g():
    with open("/home/" + username + "/.config/archmain/data/group-option.json", 'r') as f:
        return f.read()
app.after(1000, load_config_g)
option = load_config_g()


# Scrive il nuovo valore nel file di configurazione
def write_config_g(value_g):
     with open("/home/" + username + "/.config/archmain/data/group-option.json", 'w') as f:
       f.write(value_g)


# Funzione eseguita quando si seleziona un nuovo valore nell'opzione menù
def optionmenu_callback_g(choice):
    value_g = choice
    write_config_g(value_g)


def load_config_group():
    with open("/home/" + username + "/.config/archmain/data/groupname.json", 'r') as f:
        group = json.load(f)
        return group["group"]
value_c = load_config_group()

def edit_group():
    # get the value selected from the dropdown menu
    group = entry_group.get()
    # save the selected value in an external file named group
    with open("/home/" + username + "/.config/archmain/data/groupname.json", "w") as f:
      json.dump({"group": group}, f)
    

 

    # Loop through each terminal in the list
    for terminal in terminals:
        option = load_config_g()
        # Check if the terminal is installed
        if os.system(f"command -v {terminal}") == 0:
            # If the terminal is installed, run the command to update the mirrors
            os.system(f"{terminal} -e ' sudo group{option} {group}'")
            break
    # Ferma la progressbar
    progressbar.stop()
    # Nascondi la progressbar dopo 1 secondo
    app.after(1000, lambda: progressbar.place_forget())

def start_progress_bar():
    # Mostra la progressbar
    progressbar.place(x=625, y=480)
    # Avvia la progressbar
    progressbar.start()
    # Crea un nuovo thread per eseguire il comando bash
    thread = threading.Thread(target=edit_group)
    thread.start()

def change_bg_color_group(event=None):
    content = load_config_c()
    if content.islower():
        entry_group.configure(text_color=("#333","#f2f2f2"))

button = customtkinter.CTkButton(master=app,width=50,
                                 border_color="#0f94d2",
                                 
                                 fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="Group",
                                 command=start_progress_bar)
button.place(x=210, y=470)#470

entry_group = customtkinter.CTkEntry(master=app, width=120,text_color=("#06c","#2997ff"))
entry_group.insert(0, value_c) # imposta il valore iniziale
entry_group.bind("<FocusIn>", change_bg_color_group)
entry_group.place(x=345, y=470)

combobox = customtkinter.CTkComboBox(master=app,dropdown_hover_color=("#3b8ed0","#06c"),width=80,
                                         values=["add", "del"],
                                         command=optionmenu_callback_g)
combobox.place(x=263, y=470)
combobox.set(load_config_g())  # imposta il valore iniziale



#service

def load_config_s():
    with open("/home/" + username + "/.config/archmain/data/service-option.json", 'r') as f:
        return f.read()
app.after(1000, load_config_s)
option = load_config_s()


# Scrive il nuovo valore nel file di configurazione
def write_config_svr(value_s):
     with open("/home/" + username + "/.config/archmain/data/service-option.json", 'w') as f:
       f.write(value_s)


# Funzione eseguita quando si seleziona un nuovo valore nell'opzione menù
def optionmenu_callback_sv(choice):
    value_s = choice
    write_config_svr(value_s)


def load_config_service():
    with open("/home/" + username + "/.config/archmain/data/servicename.json", 'r') as f:
        servicename = json.load(f)
        return servicename["servicename"]
value_sv = load_config_service()

def edit_service():
    # get the value selected from the dropdown menu
    servicename = entry_service.get()
    # save the selected value in an external file named service
    with open("/home/" + username + "/.config/archmain/data/servicename.json", "w") as f:
      json.dump({"servicename": servicename}, f)
    

 

    # Loop through each terminal in the list
    for terminal in terminals:
        option = load_config_s()
        # Check if the terminal is installed
        if os.system(f"command -v {terminal}") == 0:
            # If the terminal is installed, run the command to update the mirrors
            os.system(f"{terminal} -e ' sudo systemctl {option} {servicename}'")
            break
    # Ferma la progressbar
    progressbar.stop()
    # Nascondi la progressbar dopo 1 secondo
    app.after(1000, lambda: progressbar.place_forget())

def start_progress_bar():
    # Mostra la progressbar
    progressbar.place(x=625, y=480)
    # Avvia la progressbar
    progressbar.start()
    # Crea un nuovo thread per eseguire il comando bash
    thread = threading.Thread(target=edit_service)
    thread.start()

def change_bg_color_service(event=None):
    content = load_config_s()
    if content.islower():
        entry_service.configure(text_color=("#333","#f2f2f2")) 

button = customtkinter.CTkButton(master=app,width=60,
                                 border_color="#0f94d2",
                                 
                                 fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="Service",
                                 command=start_progress_bar)
button.place(x=1020, y=470)

entry_service = customtkinter.CTkEntry(master=app, width=120,text_color=("#06c","#2997ff"))
entry_service.insert(0, value_sv) # imposta il valore iniziale
entry_service.bind("<FocusIn>", change_bg_color_service)
entry_service.place(x=1174, y=470)

combobox = customtkinter.CTkComboBox(master=app,dropdown_hover_color=("#3b8ed0","#06c"),width=90,
                                         values=["enable", "disable", "start", "stop", "restart"],
                                         command=optionmenu_callback_sv)
combobox.place(x=1082, y=470)
combobox.set(load_config_s())  # imposta il valore iniziale




#ProgressBar
progressbar_bk = customtkinter.CTkProgressBar(app, width=250, height=5,progress_color=("#999","#555"))
progressbar_bk.configure(mode="indeterminate")
progressbar_bk.place(x=625, y=480)
progressbar = customtkinter.CTkProgressBar(app, width=250, height=5,progress_color=("orange","#55ff00"))
progressbar.configure(mode="indeterminate")
progressbar.place_forget()




app.mainloop()
