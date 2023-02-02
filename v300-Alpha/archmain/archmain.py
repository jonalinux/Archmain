#!/usr/bin/python3
#
# Copyright (C) 2023 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>
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



import platform
import tkinter
import customtkinter
import os
import subprocess
import getpass
import tkinter as tk
from tkinter import ttk


username = getpass.getuser()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk app like you do with the Tk app
app.geometry(f"{1000}x{600}")
app.minsize(1000, 600)
app.maxsize(1000, 600)
app.title("Archmain - Archlinux Manager GUI ")
icon = tkinter.PhotoImage(file="/home/" + username + "/.config/archmain/icons/icon2.png")
app.iconphoto(False, icon)   

# configure grid layout (4x4)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

linebanner = tk.Frame(app, width=525 ,height=5, bg="#0f94d2")
linebanner.place(x=273, y=10)



# Check updates
def check_updates():
    terminal = None
    terminals = ['gnome-terminal', 'konsole', 'xfce4-terminal', 'kgx', 'lxterminal', 'alacritty',
                 'mate-terminal', 'deepin-terminal', 'qterminal', 'terminator', 'tilix', 'xterm', 'rxvt',
                 'xfterm+', 'eterm', 'st', 'aterm', 'sakura', 'lilyterm', 'cool-retro-term', 'guake', 'kitty',
                 'yakuake']
    for t in terminals:
        if os.system(f"which {t}") == 0:
            terminal = t
            break

    if terminal:
        subprocess.call([terminal, "-e", "/home/" + username + "/.config/archmain/updt"])
    else:
        print("No supported terminal found.")

def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, text="Update Now", command=check_updates)
button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

with open("/home/" + username + "/.config/archmain/data/list-upds", "r") as file:
    text = file.read()
textbox = customtkinter.CTkTextbox(app, width=250)
textbox.grid(row=0, column=1, padx=(20, 20), pady=(30, 0), sticky="nsew")
textbox.insert("0.0", text)  # insert at line 0 character 0
text = textbox.get("0.0", "end") 
textbox.configure(state="disabled")  # configure textbox to be read-only

def update_textbox():
# Console
   with open("/home/" + username + "/.config/archmain/data/list-upds", "r") as file:
    text = file.read()
   textbox = customtkinter.CTkTextbox(app, width=250)
   textbox.grid(row=0, column=1, padx=(20, 20), pady=(30, 0), sticky="nsew")
   textbox.insert("0.0", text)  # insert at line 0 character 0
   text = textbox.get("0.0", "end") 
   textbox.configure(state="disabled")  # configure textbox to be read-only
   app.after(5000, update_textbox)




#--------------------------------------------------------delay

# Carica il valore attuale dal file di configurazione
def load_config():
    with open("/home/" + username + "/.config/archmain/data/delay", 'r') as f:
        return f.read()
value = load_config()


# Scrive il nuovo valore nel file di configurazione
def write_config(value):
     with open("/home/" + username + "/.config/archmain/data/delay", 'w') as f:
       f.write(value)

# Funzione eseguita quando si seleziona un nuovo valore nel menu a tendina
def on_select(event):
    value = combobox.get()
    write_config(value)


# Crea il menu a tendina
text_var = tkinter.StringVar(value="Delay in Minutes")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               )
label.place(x=842, y=20)

combobox = customtkinter.CTkOptionMenu(app, values=["120", "180", "3600"], state='readonly')
combobox.bind("<<ComboboxSelected>>", on_select)
combobox.place(x=840, y=50)

#----------------------------------------------------------------


#---------------------------------------------------------------checkSet

# Carica il valore attuale dal file di configurazione
def load_config_2():
    with open("/home/" + username + "/.config/archmain/data/checkSet", 'r') as f:
        return f.read()
value_2 = load_config_2()


# Scrive il nuovo valore nel file di configurazione
def write_config_2(value_2):
     with open("/home/" + username + "/.config/archmain/data/checkSet", 'w') as f:
       f.write(value_2)

# Funzione eseguita quando si seleziona un nuovo valore nel menu a tendina
def on_select_2(event):
    value_2 = combobox_2.get()
    write_config_2(value_2)


# Crea il menu a tendina
text_var = tkinter.StringVar(value="Check in Minutes")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               )
label.place(x=845, y=100)

combobox_2 = customtkinter.CTkOptionMenu(app, values=["30", "60"], state='readonly')
combobox_2.bind("<<ComboboxSelected>>", on_select_2)
combobox_2.place(x=840, y=130)

#--------------------------------------------------------------------------------------------



def search_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo pikaur  {entry_value.get()}'")
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
    with open("/home/" + username + "/.config/archmain/data/ignore", "a") as f:
        f.write(f"{entry_value.get()}\n")

def downgrade_package():
    if terminal:
        os.system(f"{terminal} -e 'sudo downgrade {entry_value.get()}'")
    else:
        print("No supported terminal found.")

# Lista dei terminali
terminals = ['gnome-terminal', 'konsole', 'xfce4-terminal', 'kgx', 'lxterminal', 'alacritty',
             'mate-terminal', 'deepin-terminal', 'qterminal', 'terminator', 'tilix', 'xterm', 'rxvt',
             'xfterm+', 'eterm', 'st', 'aterm', 'sakura', 'lilyterm', 'cool-retro-term', 'guake', 'kitty',
             'yakuake']

# Seleziona il primo terminale disponibile nella lista
terminal = None
for t in terminals:
    if os.system(f"which {t}") == 0:
        terminal = t
        break

text_var = tkinter.StringVar(value="Enter the name of packages. ")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=250,
                               height=25,
                               )
label.place(x=405, y=335)

# Crea la casella di inserimento
entry_value = tk.StringVar()
entry = customtkinter.CTkEntry(app, textvariable=entry_value, width=500, height=25)
entry.place(x=285, y=360)

# Crea i bottoni
search_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), border_width=0, corner_radius=8, text="Search", command=search_package)
search_button.place(x=290, y=400)

install_button = customtkinter.CTkButton(app,width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"),  hover_color=("#3bd044","#33ad3a"), border_width=0, corner_radius=8, text="Install", command=install_package)
install_button.place(x=392, y=400)

remove_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#df4848","#df4848"), border_width=0, corner_radius=8, text="Remove", command=remove_package)
remove_button.place(x=492, y=400)

write_to_file_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#fa9b14","#c87b0c"), border_width=0, corner_radius=8, text="Ignore", command=write_to_file)
write_to_file_button.place(x=592, y=400)

downgrade_button = customtkinter.CTkButton(app, width=80, fg_color=("#ccc","#333"), text_color=("gray10", "#DCE4EE"), hover_color=("#a214fa","#a214fa"), border_width=0, corner_radius=8, text="Downgrade", command=downgrade_package)
downgrade_button.place(x=692, y=400)

def write_to_file():
    with open("/home/" + username + "/.config/archmain/data/ignore", "w") as file:
        file.write(" ")
write_to_file()


#-----------------------------------------------------------------------sidebar

# Sidebar
app.sidebar_frame = customtkinter.CTkFrame(app, width=250, corner_radius=0)
app.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
app.sidebar_frame.grid_rowconfigure(4, weight=1)


#kernel
kernel = platform.release()
label = customtkinter.CTkLabel(app.sidebar_frame, text=f"Kernel {kernel}")
label.place(x=20, y=20)

#Mirrorlist
mirrorlist = subprocess.run(['bash', '-c', 'mirrorlist=$(cat /etc/pacman.d/mirrorlist | wc -l ); diff=$( expr $mirrorlist - 10); echo $diff'], capture_output=True, text=True)
diff = int(mirrorlist.stdout.strip())
label = customtkinter.CTkLabel(app.sidebar_frame, text=f"Server Mirrors {diff}")
label.place(x=20, y=40)

#Packages







app.after(5000, update_textbox)
app.mainloop()
