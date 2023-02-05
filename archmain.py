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



#root-(app)-Archmain v3.00
app = customtkinter.CTk(className='Archmain') 
app.geometry(f"{1020}x{650}")
app.minsize(1020, 650)
app.maxsize(1020, 650)
app.title("Archmain - Arch System Management")



#user
username = getpass.getuser()

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
app.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(app,width=90,dropdown_hover_color=("#3b8ed0","#06c"), values=["Light", "Dark", "System"],
                                                              variable=appearance_mode_var,
                                                              command=lambda value: change_appearance_mode_event(value))
app.appearance_mode_optionemenu.place(x=40, y=610)

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
    with open(file_path, "w") as file:
        choice = {"appearance_mode": new_appearance_mode, "color_theme": color_theme}
        json.dump(choice, file)

label = customtkinter.CTkLabel(master=app,text="Themes", width=50, height=15, text_color="#868686")
label.place(x=55, y=590)


#terminals
with open('/home/' + username + '/.config/archmain/config/terminals.json', 'r') as file:
    terminals_dict = json.load(file)

# Accedi alla lista di terminali
terminals = terminals_dict['terminals']


# configure grid layout (4x4)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

# Sidebar
app.sidebar_frame = customtkinter.CTkFrame(app, width=170, height=390, corner_radius=12)
app.sidebar_frame.place(x=20, y=10)

# panel right
app.panel_frame = customtkinter.CTkFrame(app, width=170, height=390, corner_radius=12)
app.panel_frame.place(x=825, y=10)

#license
label = customtkinter.CTkLabel(master=app,text="Copyright (C) 2023 Jonathan Sanfilippo - GPLv3 license", width=250, height=15, text_color="#868686")
label.place(x=365, y=620)

#img "img/001.png"
pkgs = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/img/001.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/001.png"),
                                  size=(40, 40))

label001 = customtkinter.CTkLabel(app, image=pkgs, text=" ")
label001.place(x=495, y=440)


home = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/img/002.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/002.png"),
                                  size=(40, 40))

label002 = customtkinter.CTkLabel(app, image=home, text=" ")
label002.place(x=270, y=440)

orph = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/img/003.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/img/003.png"),
                                  size=(40, 40))

label003 = customtkinter.CTkLabel(app, image=orph, text=" ")
label003.place(x=710, y=440)

logo = customtkinter.CTkImage(light_image=Image.open("/home/" + username + "/.config/archmain/icons/app-logo.png"),
                                  dark_image=Image.open("/home/" + username + "/.config/archmain/icons/app-logo.png"),
                                  size=(100, 80))

label003 = customtkinter.CTkLabel(app, image=logo, text=" ", fg_color=('#dbdbdb','#2b2b2b') )
label003.place(x=56, y=300)

app.label = customtkinter.CTkLabel(app, text="Archmain v3.00", fg_color=('#dbdbdb','#2b2b2b'), text_color="#868686")
app.label.place(x=60, y=370)


#ProgressBar
progressbar = customtkinter.CTkProgressBar(app, width=250, height=5,progress_color="#55ff00")
progressbar.configure(mode="indeterminate",)
progressbar.place_forget()

#Update Now
def check_updates():
    terminal = None
    for t in terminals:
        if os.system(f"which {t}") == 0:
            terminal = t
            break

    if terminal:
        subprocess.call([terminal, "-e", "/home/" + username + "/.config/archmain/scripts/updatenow"])
    else:
        print("No supported terminal found.")
        
        
def button_function():
    print("button pressed")

button = customtkinter.CTkButton(app, border_color="#0f94d2",  text_color=("#DCE4EE", "#DCE4EE"), border_width=0, corner_radius=4, text="Update Now", command=check_updates)
button.place(x=35, y=20)





#ignore-AUR
def ignore_AUR():
    terminal = None
    for t in terminals:
        if os.system(f"which {t}") == 0:
            terminal = t
            break

    if terminal:
        subprocess.call([terminal, "-e", "/home/" + username + "/.config/archmain/scripts/ignore-AUR"])
    else:
        print("No supported terminal found.")
        
        
def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, border_color="#0f94d2", fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), border_width=0, corner_radius=4, text="Ignore AUR", command=ignore_AUR)
button.place(x=35, y=53)



#manual-Check
def man_check_updates():
    subprocess.call(["bash", "/home/" + username + "/.config/archmain/scripts/verified"])
    progressbar.stop()
    app.after(1000, lambda: progressbar.place_forget())

def start_progress_bar():
    progressbar.place(x=390, y=586)
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
                                 command=start_progress_bar)
button.place(x=35, y=86)


#New-mirrors
def load_config_c():
    with open("/home/" + username + "/.config/archmain/config/country.json", 'r') as f:
        country = json.load(f)
        return country["country"]
value_c = load_config_c()


# lista delle opzioni per il menu a tendina
with open('/home/' + username + '/.config/archmain/config/lang.json', 'r') as file:
    countries_dict = json.load(file)

# Accedi alla lista di terminali
countries = countries_dict['countries']



def new_mirrors():
    # get the value selected from the dropdown menu
    country = combobox_country.get()
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
    progressbar.place(x=390, y=586)
    # Avvia la progressbar
    progressbar.start()
    # Crea un nuovo thread per eseguire il comando bash
    thread = threading.Thread(target=new_mirrors)
    thread.start()

button = customtkinter.CTkButton(master=app,width=90,
                                 border_color="#0f94d2",
                                 fg_color=("#ccc","#333"),
                                 text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4,
                                 text="New Mirrors",
                                 command=start_progress_bar)
button.place(x=35, y=119)

combobox_country = customtkinter.CTkOptionMenu(master=app, width=50, dropdown_hover_color=("#3b8ed0","#06c"),values=countries)
combobox_country.place(x=128, y=119)
combobox_country.set(value_c)  # imposta il valore iniziale 



#leggi pacchetti
def read_text_file():
    try:
        with open('/home/' + username + '/.config/archmain/data/last.json', 'r') as file:
            text = file.read()
            with open("/home/" + username + "/.config/archmain/data/console.json", "w") as file:
                file.write(text)
    except:
        print("Error reading/writing file")

read_text_file_button = customtkinter.CTkButton(app, border_color="#0f94d2",
                                 fg_color=("#ccc","#333"),
                                 text_color=("gray10", "#DCE4EE"),
                                 border_width=0,
                                 corner_radius=4, text="Last Updated", command=read_text_file)
read_text_file_button.place(x=35, y=152)



#Console
text = ""

def update_textbox():
   global text
   with open("/home/" + username + "/.config/archmain/data/console.json", "r") as file:
      new_text = file.read()
   if new_text != text:
      textbox.configure(state="normal")  # configure textbox to be editable
      textbox.delete("0.0", "end")  # clear textbox
      textbox.insert("0.0", new_text)  # insert updated text
      textbox.configure(state="disabled")  # configure textbox to be read-only
      text = new_text
   app.after(1000, update_textbox)

textbox = customtkinter.CTkTextbox(app, width=600, height=350, font=('source code pro',14), corner_radius=12)
textbox.place(x=207, y=50)
textbox.configure(state="disabled") # configure textbox to be read-only
app.after(1000, update_textbox)



def del_console():
    with open("/home/" + username + "/.config/archmain/data/console.json", "w") as file:
        file.write(" ")

button = customtkinter.CTkButton(master=app, text="Clean Console",text_color=("gray10", "#DCE4EE"), fg_color=("#ccc","#333"),hover_color=("#df4848","#df4848"),command=del_console)
button.place(x=850, y=610)




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
text_var = tkinter.StringVar(value="Notify Delay in Min")

label = customtkinter.CTkLabel(master=app,textvariable=text_var,width=120,height=25, fg_color=('#dbdbdb','#2b2b2b'))
label.place(x=842, y=20)

combobox = customtkinter.CTkOptionMenu(master=app,dropdown_hover_color=("#3b8ed0","#06c"),
                                         values=["120", "180", "240","1440"],
                                         command=optionmenu_callback)
combobox.place(x=840, y=48)
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
text_var = tkinter.StringVar(value="Check every Min")

label = customtkinter.CTkLabel(master=app,textvariable=text_var, width=120,height=25,fg_color=('#dbdbdb','#2b2b2b'))
label.place(x=845, y=90)

combobox_2 = customtkinter.CTkOptionMenu(master=app,dropdown_hover_color=("#3b8ed0","#06c"),
                                         values=["60", "120", "180","1440"],
                                         command=optionmenu_callback_2)
combobox_2.place(x=840, y=118)
combobox_2.set(load_config_2())  # imposta il valore iniziale


#-Ricerca multi-opzioni
def search_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur {entry_value.get()}'")
    else:
        print("No supported terminal found.")

def install_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur -S {entry_value.get()}'")
    else:
        print("No supported terminal found.")

def remove_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur -Rns {entry_value.get()}'")
    else:
        print("No supported terminal found.")

def write_to_file():
    with open("/home/" + username + "/.config/archmain/data/ignore.json", "a") as f:
        f.write(f"{entry_value.get()}\n")

def downgrade_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo downgrade {entry_value.get()}'")
    else:
        print("No supported terminal found.")

terminal = None 
for t in terminals: 
    if os.system(f"which {t}") == 0:
        terminal = t
        break


#entry = customtkinter.CTkEntry(app, textvariable=entry_value, width=400, height=29, text_color=("#06c","#2997ff"))
#entry.place(x=263, y=12)

def clear_entry():
    entry_value.set("")
button = customtkinter.CTkButton(master=app, width=50, text="Del",text_color=("gray10", "#DCE4EE"), fg_color=("#ccc","#333"),hover_color=("#df4848","#df4848"),command=clear_entry)
button.place(x=210, y=12)    

def change_bg_color(event=None):
    content = entry_value.get()
    if content.islower():
        entry.configure(text_color=("#333","#f2f2f2"))
    else:
        entry.configure(text_color=("#df4848"))
    return content.islower()

entry_value = tk.StringVar()
entry_value.set("before using the options, insert the package name.")
entry = customtkinter.CTkEntry(app, textvariable=entry_value, width=400, height=29, text_color=("#06c","#2997ff"))
entry.place(x=263, y=12)
entry.bind("<FocusIn>", change_bg_color)
entry.bind("<KeyRelease>", change_bg_color)


actions = ['Search', 'Install', 'Remove', '--Ignore', 'Downgrade']
combobox_var = customtkinter.StringVar(value="Options")

def combobox_callback(choice):
    if choice == 'Search':
        search_package()
    elif choice == 'Install':
        install_package()
    elif choice == 'Remove':
        remove_package()
    elif choice == 'Ignore':
        write_to_file()
    elif choice == 'Downgrade':
        downgrade_package()

combobox = customtkinter.CTkComboBox(master=app, dropdown_hover_color=("#3b8ed0","#06c"), values=actions, variable=combobox_var, command=combobox_callback)
combobox.place(x=665, y=12)

def reset():
    with open("/home/" + username + "/.config/archmain/data/ignore.json", "w") as file:
        file.write("")
reset()


#cpu-disk-ram-swap-boot
def update_values():
    disk_usage = psutil.disk_usage("/").percent
    disk_progress.set(value=disk_usage/100)
    disk_label.configure(text="Disk Usage: {:.2f}%".format(disk_usage))

    ram_usage = psutil.virtual_memory().percent
    ram_progress.set(value=ram_usage/100)
    ram_label.configure(text="RAM Usage: {:.2f}%".format(ram_usage))

    swap_usage = psutil.swap_memory().percent
    swap_progress.set(value=swap_usage/100)
    swap_label.configure(text="Swap Usage: {:.2f}%".format(swap_usage))
    
    cpu_usage = psutil.cpu_percent()
    cpu_progress.set(value=cpu_usage/100)
    cpu_label.configure(text="CPU Usage: {:.2f}%".format(cpu_usage))
 
    boot_partition_usage = psutil.disk_usage("/boot").percent
    boot_partition_progress.set(value=boot_partition_usage/100)
    boot_partition_label.configure(text="Boot Partition: {:.2f}%".format(boot_partition_usage))

    app.after(1000, update_values)


app.after(1000, update_values)

cpu_label = customtkinter.CTkLabel(app, text="CPU Usage:" , fg_color=('#dbdbdb','#2b2b2b'))
cpu_label.place(x=845, y=237)

cpu_progress = customtkinter.CTkProgressBar(app, height=5, width=130, progress_color="red")
cpu_progress.place(x=845, y=260)

disk_label = customtkinter.CTkLabel(app, text="Disk Usage:", fg_color=('#dbdbdb','#2b2b2b'))
disk_label.place(x=845, y=267)

disk_progress = customtkinter.CTkProgressBar(app, height=5, width=130, progress_color="#0f94d2")
disk_progress.place(x=845, y=290)

ram_label = customtkinter.CTkLabel(app, text="RAM Usage:", fg_color=('#dbdbdb','#2b2b2b'))
ram_label.place(x=845, y=297)

ram_progress = customtkinter.CTkProgressBar(app, height=5,width=130, progress_color="orange")
ram_progress.place(x=845, y=320)

swap_label = customtkinter.CTkLabel(app, text="Swap Usage:", fg_color=('#dbdbdb','#2b2b2b'))
swap_label.place(x=845, y=327)

swap_progress = customtkinter.CTkProgressBar(app, height=5,width=130, progress_color="magenta")
swap_progress.place(x=845, y=350)

boot_partition_label = customtkinter.CTkLabel(app, text="Boot Partition Usage:", fg_color=('#dbdbdb','#2b2b2b'))
boot_partition_label.place(x=845, y=357)

boot_partition_progress = customtkinter.CTkProgressBar(app, height=5,width=130, progress_color="#55ff00")
boot_partition_progress.place(x=845, y=380)

def count_installed_packages():
    output = subprocess.run(['pikaur', '-Q'], stdout=subprocess.PIPE)
    packages = output.stdout.decode('utf-8').split('\n')
    return len(packages)


def update_kernel_info():
    kernel = platform.release()
    kernel_label.configure(text="Kernel: {}".format(kernel))
    kernel_label.after(1000, update_kernel_info)
    
kernel_label = customtkinter.CTkLabel(app, text="Kernel: ...", fg_color=('#dbdbdb','#2b2b2b'))
kernel_label.place(x=845, y=165)
app.after(1000, update_kernel_info)

def update_mirrorlist_info():
    mirrorlist = subprocess.run(['bash', '-c', 'mirrorlist=$(cat /etc/pacman.d/mirrorlist | wc -l ); diff=$( expr $mirrorlist - 10); echo $diff'], capture_output=True, text=True)
    diff = int(mirrorlist.stdout.strip())
    mirrorlist_label.configure(text="Server Mirrors: {}".format(diff))
    mirrorlist_label.after(1000, update_mirrorlist_info)

mirrorlist_label = customtkinter.CTkLabel(app, text="Server Mirrors: ...", fg_color=('#dbdbdb','#2b2b2b'))
mirrorlist_label.place(x=845, y=185)
app.after(1000, update_mirrorlist_info)

def update_packages_info():
    packages = count_installed_packages()
    label.configure(text="Packages: {}".format(packages))
    label.after(1000, update_packages_info)

label = customtkinter.CTkLabel(app,fg_color=('#dbdbdb','#2b2b2b'),text="Packages: {}".format(count_installed_packages()))
label.place(x=845, y=205)
app.after(1000, update_packages_info)


#cache-home-bin
def get_cache_and_trash_size():
    result = subprocess.check_output(["du", "-sh", "/home/" + username + "/.cache/", "/home/" + username + "/.local/share/Trash/"])
    sizes = result.splitlines()
    cache_size = sizes[0].split()[0].decode("utf-8")
    trash_size = sizes[1].split()[0].decode("utf-8")
    return cache_size, trash_size

def clear_cache_and_trash():
    os.system("rm -rf ~/.cache/*")
    os.system("rm -rf ~/.local/share/Trash/*")
    update_info_label()

def update_info_label():
    cache_size, trash_size = get_cache_and_trash_size()
    text_var2.set("Cache home: " + cache_size + "B\nTrash: " + trash_size + "B")

text_var2 = customtkinter.StringVar(value="Cache size: updating...\nTrash size: updating...")

info_label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var2,
                               width=120,
                               height=40)
info_label.place(x=230, y=520)

clear_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Clear", command=clear_cache_and_trash)
clear_button.place(x=250, y=490)

app.after(1000, update_info_label)

update_info_label()

def update_info_label():
    cache_size, trash_size = get_cache_and_trash_size()
    text_var2.set("Cache home: " + cache_size + "B\nTrash: " + trash_size + "B")
    app.after(1000, update_info_label) # Aggiungi questa riga

app.after(1000, update_info_label)


#Cache-Packages
def clear_cache_pkg():
    for terminal in terminals:
        try:
            if terminal == 'gnome-terminal':
                subprocess.call([terminal, '-e', "sudo pikaur -Sc"])
            else:
                subprocess.call([terminal, '-e', 'sudo pikaur -Sc'])
            break
        except:
            continue
                
    update_label()
clean_cache_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Clear",  command=clear_cache_pkg)
clean_cache_button.place(x=475, y=490)

#mostra valore cache
def get_cache_size():
    result = subprocess.check_output(["du", "-sh", "/var/cache/pacman/pkg/"])
    size = result.split()[0].decode("utf-8")
    return size


def update_label():
    size = get_cache_size()
    text_var.set("Cache Pkgs: " + size + "B")
    app.after(1000, update_label)
    
text_var = tkinter.StringVar(value="Cache size: updating...")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=250,
                               height=25,
                               )
label.place(x=390, y=520)
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
            else:
                subprocess.call([terminal, '-e', "/home/" + username + "/.config/archmain/scripts/remove-orphans"])
            
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

# Creazione del bottone per pulire la cache dei pacchetti orfani
clear_orphan_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Remove", command=clear_orphan_pkgs)
clear_orphan_button.place(x=690, y=490)

# Creazione della label che mostra il numero di pacchetti orfani
orphan_pkgs_label = customtkinter.CTkLabel(app, textvariable=orphan_pkgs_label_text, width=120, height=25)
orphan_pkgs_label.place(x=670, y=520)
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






app.mainloop()
