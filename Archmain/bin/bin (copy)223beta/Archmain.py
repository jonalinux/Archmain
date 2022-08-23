#!/usr/bin/python
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



from time import sleep
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import getpass
from tokenize import Number
from turtle import width
import webbrowser
from xmlrpc import server
import time

window=tk.Tk(className='Archmain')
window.title('Archmain')
window.geometry("800x600+10+20")
window.maxsize(850, 620)
window.minsize(850, 620)
window.configure(bg='#f6f9fc')
username = getpass.getuser()
p1 = PhotoImage(file="/home/" + username + "/.local/share/Archmain/icon/icon2.png")
window.iconphoto(False, p1)   


#top-footer
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
footer.place(x=0, y=590)
version = tk.Label(master=window, text="Version", font=('SF Pro Display',8), bg="#ecf2f5", fg="#666")
version.place(x=773, y=595)
numversion = Text(window,  font=('SF Pro Display',10), bg="#ecf2f5", fg="#0f94d2", borderwidth = 0, highlightthickness = 0)
numversion.place(x=815, y=595)
author = tk.Label(master=window, text="© 2022 Jonathan Sanfilippo", font=('SF Pro Display',8), bg="#ecf2f5", fg="#666")
author.place(x=10, y=595)



def callback(url):
   webbrowser.open_new_tab(url)
   
link = Label(window, text="GitHub",font=('SF Pro Display', 8), bg="#ecf2f5", fg="#0f94d2")
link.place(x=150, y=596)
link.bind("<Button-1>", lambda e:
callback("https://github.com/JonathanSanfilippo/Archmain"))

github = open(file="/home/" + username + "/.local/share/Archmain/data/currentVersion")
for ver in github:
   numversion.insert(END, ver )
numversion.config(state=DISABLED)

#-------------------------------------------------------------------------------------------------------------------------





#Install or remove packages:
def InsRmv(): 
    package=form.get()
    option=options.get()
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "/usr/bin/pikaur ' + option + ' ' + package + ' " ')
   

background_form = tk.Frame(master=window, width=378, height=70, bg="#0f94d2")
background_form.place(x=430, y=0)
options = tk.Entry(window, width=6, bg="#fff", fg='#555', font=('SF Pro Display',11), )
options.place(x=440, y=40)
options.insert(0," -S") 
form = tk.Entry(window, width=25, bg="#fff", fg='#555', font=('SF Pro Display',11), )
form.place(x=510, y=40)
form.insert(0," package name ") 
form_title = tk.Label(master=window, text="Install or remove packages", font=('SF Pro Display',10), bg="#0f94d2", fg="#fff")
form_title.place(x=440, y=12)
btnPkgs=tk.Button(window,  height=1, width=3, text="Run", bg='#dfd' , fg="#555", font=('SF Pro Display',10), borderwidth = 0, highlightthickness = 0, command=InsRmv)
btnPkgs.place(x=750, y=39)

#-------------------------------------------------------------------------------------------------------------------------



def list_upd(): #-----------------------------------------------------------------------------console
 background_lista = tk.Frame(master=window, width=528, height=300, bg="#ecf2f5")
 background_lista.place(x=30, y=100,)
 background_lista.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
 content = open(file="/home/" + username + "/.local/share/Archmain/data/listupdates")
 lista=Text(master=window,  width=63, height=17,font=('SF Pro Display',10), bg='#ecf2f5', fg="#555", borderwidth = 0, highlightthickness = 0, )
 lista.place(x=40, y=105,)

 for updates in content:
   lista.insert(END, updates )
 lista.config(state=DISABLED)
 window.after(5000, list_upd)
#-------------------------------------------------------------------------------------------------------------------------





#linee install + check
lineah=tk.Frame(window, height=1, width=650, bg="#999").place(x=60, y=449,)
lineav1=tk.Frame(window, height=15, width=1, bg="#999").place(x=60, y=435,)
lineav2=tk.Frame(window, height=15, width=1, bg="#999").place(x=140, y=435,)
lineav3=tk.Frame(window, height=60, width=1, bg="#999").place(x=359, y=460,)
lineav4=tk.Frame(window, height=45, width=1, bg="#999").place(x=80, y=450,)
label=tk.Label(window, text="Last ",font=('SF Pro Display',10), fg="#999", bg='#f6f9fc').place(x=155, y=438,)
lineah2=tk.Frame(window, height=1, width=200, bg="#999").place(x=290, y=515,)
lineah3=tk.Frame(window, height=1, width=70, bg="#999").place(x=395, y=482,)

#Rollback 
def rollback_set():
 result=rollback_label.get() 
 os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");    $TERMINAL "sudo downgrade '+ result + ' "' )

rollback_label = Entry(master=window,  width=20,font=('SF Pro Display',10), bg="#ecf2f5", fg="#555", borderwidth = 0, highlightthickness = 0 )
rollback_label.place(x=650, y=438,)
rollback_label.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
btn=tk.Button(window, height=1, width=6, text="Rollback", font=('SF Pro Display',10),bg='#fed882' , fg="#555", borderwidth = 0, highlightthickness = 0, command=rollback_set)
btn.place(x=570, y=435,)
rollback_label.insert(0, ' package name')



# bottom install only pacman 
def install_pac():
    cmdx="AUR=$(pikaur -Qqua ;) TERMINAL=$(cat $HOME/.local/share/Archmain/data/terminal);"
    urltemp="/home/'"+username+"'/.local/share/Archmain/data/temp"
    os.system( cmdx + '$TERMINAL  "echo Writing a log file; echo $(date) > '+ urltemp+ '; echo  last updates >> ' + urltemp + ';  checkupdates   >> ' + urltemp + ' ; sudo pacman -Syu;  mv ' + urltemp + '  /home/' + username + '/.local/share/Archmain/data/@lastup;";echo "Waiting for next check" > /home/' + username + '/.local/share/Archmain/data/listupdates; echo "Waiting for next check" > /home/' + username + '/.local/share/Archmain/data/pending; ')
    
btnInstall=tk.Button(window, height=1, width=8, text="Exclude AUR", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=install_pac)
btnInstall.place(x=100, y=405,)

# bottom install updates
def install_Updates():
    cmdx="AUR=$(pikaur -Qqua ;) TERMINAL=$(cat $HOME/.local/share/Archmain/data/terminal);"
    urltemp="/home/'"+username+"'/.local/share/Archmain/data/temp"
    os.system( cmdx + '$TERMINAL  "echo Writing a log file; echo $(date) > '+ urltemp+ '; echo  last updates >> ' + urltemp + ';  checkupdates   >> ' + urltemp + ' ; /usr/bin/pikaur -Syu;  mv ' + urltemp + '  /home/' + username + '/.local/share/Archmain/data/@lastup;";echo "Waiting for next check" > /home/' + username + '/.local/share/Archmain/data/listupdates; echo "Waiting for next check" > /home/' + username + '/.local/share/Archmain/data/pending; ')
    #os.system(' AUR=$(pikaur -Qqua ;) TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "echo Writing a log file; echo $(date) > /home/' + username + '/.local/share/Archmain/data/temp ;echo  last updates >>  /home/' + username + '/.local/share/Archmain/data/temp;  pacman -Qu    >>  /home/' + username + '/.local/share/Archmain/data/temp; /usr/bin/pikaur -Syu;   mv /home/' + username + '/.local/share/Archmain/data/temp  /home/' + username + '/.local/share/Archmain/data/@lastup;  "; echo "Waiting for next check" > /home/' + username + '/.local/share/Archmain/data/listupdates; echo "Waiting for next check" > /home/' + username + '/.local/share/Archmain/data/pending; ')
    
btnInstall=tk.Button(window, height=1, width=5, text="Install", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=install_Updates)
btnInstall.place(x=30, y=405,)


#@lastup
def log():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("x.Horizontal.TProgressbar", foreground='x', background='#fed882', troughcolor='#ecf2f5', bordercolor='#bbccdd')
    progress=ttk.Progressbar(window,style="x.Horizontal.TProgressbar", orient=HORIZONTAL,length=200,mode='determinate')
    progress.place(x=250, y=595)
    labprogress=tk.Entry(window, width=4, font=('SF Pro Display',8), bg="#ecf2f5", fg="#666", borderwidth = 0, highlightthickness = 0)
    labprogress.insert(0," ")
    labprogress.place(x=460, y=595)
    import time
    progress['value'] = 5
    labprogress.insert(0,"5%     ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 30
    labprogress.insert(0,"30%     ")
    window.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.5)
    
    os.system('cp  /home/' + username + '/.local/share/Archmain/data/@lastup  /home/' + username + '/.local/share/Archmain/data/listupdates; ')

    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(1.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)


btnInstall=tk.Button(window, height=1, width=7, text="Last Update", font=('SF Pro Display',10), bg='#fed882', fg="#555", borderwidth = 0, highlightthickness = 0, command=log)
btnInstall.place(x=60, y=485,)



# bottom mirrorlist •
def mirrorlist():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("x.Horizontal.TProgressbar", foreground='x', background='#aad0fd', troughcolor='#ecf2f5', bordercolor='#bbccdd')
    progress=ttk.Progressbar(window,style="x.Horizontal.TProgressbar", orient=HORIZONTAL,length=200,mode='determinate')
    progress.place(x=250, y=595)
    labprogress=tk.Entry(window, width=4, font=('SF Pro Display',8), bg="#ecf2f5", fg="#666", borderwidth = 0, highlightthickness = 0)
    labprogress.insert(0," ")
    labprogress.place(x=460, y=595)
    import time
    progress['value'] = 5
    labprogress.insert(0,"5%     ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 30
    labprogress.insert(0,"30%     ")
    window.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.5)
  
    os.system(' TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");  SRV=$(rankmirrors -t   /etc/pacman.d/mirrorlist | wc -l );   Srv=$( expr $SRV - 3);   echo  $Srv  >  /home/' + username + '/.local/share/Archmain/data/server;  rankmirrors -t   /etc/pacman.d/mirrorlist  > /home/' + username + '/.local/share/Archmain/data/listupdates;  ')
    
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(1.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)

btn=tk.Button(window, height=1, width=7, text="Mirrorlist", font=('SF Pro Display',10), bg='#aad0fd', fg="#555", borderwidth = 0, highlightthickness = 0, command=mirrorlist)
btn.place(x=318, y=468,)
server=Label(window, height=1, text="Server", font=('SF Pro Display',10), bg='#f6f9fc', fg="#999", borderwidth = 0, highlightthickness = 0)
server.place(x=414, y=472,)



def currServer():
 server_c=open(file="/home/" + username + "/.local/share/Archmain/data/server")   
 server_current = Text(master=window,  height=1, width=4,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
 server_current.place(x=459, y=472.4)

 for S in server_c:
  server_current.insert(END, S)
  server_current.config(state=DISABLED)
 window.after(5000, currServer)


#Reflector mirrors
def reflector():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("x.Horizontal.TProgressbar", foreground='x', background='#fed882', troughcolor='#ecf2f5', bordercolor='#bbccdd')
    progress=ttk.Progressbar(window,style="x.Horizontal.TProgressbar", orient=HORIZONTAL,length=200,mode='determinate')
    progress.place(x=250, y=595)
    labprogress=tk.Entry(window, width=4, font=('SF Pro Display',8), bg="#ecf2f5", fg="#666", borderwidth = 0, highlightthickness = 0)
    labprogress.insert(0," ")
    labprogress.place(x=460, y=595)
    import time
    progress['value'] = 5
    labprogress.insert(0,"5%     ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 30
    labprogress.insert(0,"30%     ")
    window.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.5)

    C=country.get() 
    os.system(' TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");   $TERMINAL  "sudo reflector --verbose --country  '  +  C  + '   --age 12 --sort rate --save /etc/pacman.d/mirrorlist; "')
    os.system('SRV=$(rankmirrors -t   /etc/pacman.d/mirrorlist | wc -l );  Srv=$( expr $SRV - 3);   echo $Srv >  /home/' + username + '/.local/share/Archmain/data/server; ')
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(1.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)


country=Entry(window,  width=4,font=('SF Pro Display',10), bg="#ecf2f5", fg="#555",borderwidth = 0, highlightthickness = 0)
country.place(x=270, y=505,)
country.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
country.insert(0, " gb")
btn=tk.Button(window, height=1, width=7, text="Reflector", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=reflector).place(x=318, y=502,)
info=Label(window, font=('SF Pro Display',9), bg='#f6f9fc', fg="#888", text="Select the HTTP / HTTPS mirrors synchronized in the last 12 hours \n and located according  to the chosen country and overwrite \n the /etc/pacman.d/mirrorlist file with the results.")
info.place(x=410, y=505,)

# bottom install only pacman
def Check_now():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("x.Horizontal.TProgressbar", foreground='x', background='#87ffc1', troughcolor='#ecf2f5', bordercolor='#bbccdd')
    progress=ttk.Progressbar(window,style="x.Horizontal.TProgressbar", orient=HORIZONTAL,length=200,mode='determinate')
    progress.place(x=250, y=595)
    labprogress=tk.Entry(window, width=4, font=('SF Pro Display',8), bg="#ecf2f5", fg="#666", borderwidth = 0, highlightthickness = 0)
    labprogress.insert(0," ")
    labprogress.place(x=460, y=595)
    import time
    progress['value'] = 5
    labprogress.insert(0,"5%     ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 30
    labprogress.insert(0,"30%     ")
    window.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.5)
  
    os.system('/home/' + username + '/.local/share/Archmain/bin/chnw.sh')

    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(1.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)
    
btn=tk.Button(window, height=1, width=7, text="Check Now", font=('SF Pro Display',10), bg='#87ffc1', fg="#555", borderwidth = 0, highlightthickness = 0, command=Check_now)
btn.place(x=318, y=435,)

def last_chk():
 lastcheck = open(file="/home/" + username + "/.local/share/Archmain/data/lastcheck")
 lastcheck_label = Text(master=window,  width=14, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 lastcheck_label.place(x=185, y=439)

 for info_lastcheck in lastcheck:
  lastcheck_label.insert(END, info_lastcheck )
  lastcheck_label.config(state=DISABLED)
 window.after(5000, last_chk); 

def message_Delay():
 messageDelay = open(file="/home/" + username + "/.local/share/Archmain/data/messageDelay")
 messageDelay_label_title = tk.Label(master=window, text="Next ", font=('SF Pro Display',10), bg="#f6f9fc", fg="#999")
 messageDelay_label_title.place(x=415, y=438)
 messageDelay_label = Text(master=window,  width=14, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="orangered", borderwidth = 0, highlightthickness = 0,)
 messageDelay_label.place(x=447, y=439)

 for info_messageDelay in messageDelay:
  messageDelay_label.insert(END, info_messageDelay )
  messageDelay_label.config(state=DISABLED)
 window.after(5000, message_Delay); 



 #pending-updates
def pending_upd():
 pending = open(file="/home/" + username + "/.local/share/Archmain/data/pending")
 pending_label_title = tk.Label(master=window, text="Status:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 pending_label_title.place(x=580, y=103)
 pending_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 pending_label.place(x=627, y=105)

 for info_pending in pending:
   pending_label.insert(END, info_pending )
 pending_label.config(state=DISABLED)
 window.after(5000, pending_upd)





#-------------------------------------------------------------------------------------------------------------------------




def kernel_upd():
 krn="Kernel=$(uname -r ); kernel=$HOME/.local/share/Archmain/data/kernel ;"
 os.system( krn + '  echo $Kernel > $kernel')
 kernel = open(file="/home/" + username + "/.local/share/Archmain/data/kernel")
 kernel_label_title = tk.Label(master=window, text="kernel:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 kernel_label_title.place(x=580, y=133)
 kernel_label = Text(master=window,  width=90, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 kernel_label.place(x=627, y=135)

 for info_kernel in kernel:
   kernel_label.insert(END, info_kernel )
 kernel_label.config(state=DISABLED)
 window.after(60000,kernel_upd)

def pkgs_upd():
 pax="PackagesTotal=$(pacman -Q | wc -l ); packages=$HOME/.local/share/Archmain/data/packages ; "
 os.system( pax + '  echo "$PackagesTotal" > "$packages"')
 pkgs_count = open(file="/home/" + username + "/.local/share/Archmain/data/packages")
 pkgs_count_label_title = tk.Label(master=window, text="Installed Packages:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 pkgs_count_label_title.place(x=580, y=163)
 pkgs_count_label = Text(master=window,  width=4, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 pkgs_count_label.place(x=697, y=165)

 for info_pkgs_count in pkgs_count:
   pkgs_count_label.insert(END, info_pkgs_count )
 pkgs_count_label.config(state=DISABLED)
 window.after(5000, pkgs_upd)


   
def ram_upd(): 
 ramy=" RM=$HOME/.local/share/Archmain/data/ram  ; "
 ramx="Ram=$(free -h | grep G | awk -F" + "'i       '"  +  " '{ print $2 }');"   
 os.system( ramx + ramy +   ' echo "$Ram" > "$RM"'  )
 ram = open(file="/home/" + username + "/.local/share/Archmain/data/ram")
 ram_label_title = tk.Label(master=window, text="Memory usage:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 ram_label_title.place(x=580, y=193)
 ram_label = Text(master=window,  width=5, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 ram_label.place(x=675, y=195)

 for info_ram in ram:
   ram_label.insert(END, info_ram )
   ram_label.config(state=DISABLED)
 window.after(5000, ram_upd)

def ssd_upd():
 ssdx="SSD=$(df -h / | grep G|awk '{printf $3}')"
 os.system( ssdx + " ssd=$HOME/.local/share/Archmain/data/ssd;   echo  $SSD > $ssd")
 ssd = open(file="/home/" + username + "/.local/share/Archmain/data/ssd")
 ssd_label_title = tk.Label(master=window, text="Disc usage:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 ssd_label_title.place(x=580, y=223)
 ssd_label = Text(master=window,  width=10, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 ssd_label.place(x=650, y=225)

 for info_ssd in ssd:
   ssd_label.insert(END, info_ssd )
 ssd_label.config(state=DISABLED)
 window.after(5000, ssd_upd)

def cache_upd():
 chx="Cache=$( du -sh $HOME/.cache/ | awk '{ printf $1}'); cache=$HOME/.local/share/Archmain/data/cache ;"
 os.system( chx + ' echo "$Cache" > "$cache"')
 cache = open(file="/home/" + username + "/.local/share/Archmain/data/cache")
 cache_label_title = tk.Label(master=window, text="Cache:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 cache_label_title.place(x=580, y=253)
 cache_label = Text(master=window,  width=13, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 cache_label.place(x=626, y=255)

 for info_cache in cache:
   cache_label.insert(END, info_cache )
 cache_label.config(state=DISABLED)
 window.after(5000, cache_upd)

def orphans_upd():
 orph="Orphans=$(pacman -Qtdq | wc -l); orphans=$HOME/.local/share/Archmain/data/orphans ;"
 os.system( orph + ' echo "$Orphans" > "$orphans"')
 orphans = open(file="/home/" + username + "/.local/share/Archmain/data/orphans")
 orphans_label_title = tk.Label(master=window, text="Unused (orphans):", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 orphans_label_title.place(x=580, y=283)
 orphans_label = Text(master=window,  width=4, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 orphans_label.place(x=690, y=285)

 for info_orphans in orphans:
   orphans_label.insert(END, info_orphans )
 orphans_label.config(state=DISABLED)
 window.after(5000, orphans_upd)

def cachePac_upd():
 cpax="CachePacman=$(du -sh  /var/cache/pacman/pkg  | awk '{ printf $1}');  cachepacman=$HOME/.local/share/Archmain/data/cachepacman ;"
 os.system( cpax + '  echo "$CachePacman" > "$cachepacman"')
 cachePacman = open(file="/home/" + username + "/.local/share/Archmain/data/cachepacman")
 cachePacman_label_title = tk.Label(master=window, text="Packages Cache:", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 cachePacman_label_title.place(x=580, y=313)
 cachePacman_label = Text(master=window,  width=5, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 cachePacman_label.place(x=685, y=315)

 for info_cachePacman in cachePacman:
   cachePacman_label.insert(END, info_cachePacman )
 cachePacman_label.config(state=DISABLED)
 window.after(5000, cachePac_upd)


#check
def checkSet_set():
 result=checkSet_label.get() 
 os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/checkSet;")
  
checkSet=open(file="/home/" + username + "/.local/share/Archmain/data/checkSet")    
checkSet_label_title = tk.Label(master=window, text="Check", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
checkSet_label_title.place(x=580, y=352)
checkSet_label = Entry(master=window,  width=4,font=('SF Pro Display',10), bg="#ecf2f5", fg="green", borderwidth = 0, highlightthickness = 0, )
checkSet_label.place(x=620, y=352)
checkSet_label.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")

btnSet=tk.Button(window,  height=1, width=1, text="Set", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=lambda:[checkSet_set()])
btnSet.place(x=660, y=350)

def status_check():
  statuscheck = open(file="/home/" + username + "/.local/share/Archmain/data/checkSet")
  statuscheck_label = Text(master=window,  height=1, width=4,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
  statuscheck_label.place(x=755,  y=354)
  statuscheck_title = tk.Label(master=window, text="Min", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
  statuscheck_title.place(x=730, y=353)
  statusch2_label = tk.Label(master=window,  text="∞", width=3, height=1,font=('SF Pro Display',15), bg="#f6f9fc", fg="grey", borderwidth = 0, highlightthickness = 0,)
  statusch2_label.place(x=694,  y=348)

  for info_statuscheck in statuscheck:
   statuscheck_label.insert(END, info_statuscheck )
   statuscheck_label.config(state=DISABLED)
   window.after(2500, status_check); 


#delay
def delay_set():
 result=delay_label.get() 
 os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/delay;")
  
delay=open(file="/home/" + username + "/.local/share/Archmain/data/delay")    
delay_label_title = tk.Label(master=window, text="Delay", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
delay_label_title.place(x=580, y=382)
delay_label = Entry(master=window,  width=4,font=('SF Pro Display',10), bg="#ecf2f5", fg="green", borderwidth = 0, highlightthickness = 0, )
delay_label.place(x=620, y=382)
delay_label.config( highlightthickness=1,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")

btnSet=tk.Button(window,  height=1, width=1, text="Set", font=('SF Pro Display',10), bg='#dfd', fg="#555", borderwidth = 0, highlightthickness = 0, command=lambda:[delay_set()])
btnSet.place(x=660, y=380)

   
def currDelay():
 delay_c=open(file="/home/" + username + "/.local/share/Archmain/data/delay")   
 delay_current2_title = tk.Label(master=window, text="Min", font=('SF Pro Display',10), bg="#f6f9fc", fg="#555")
 delay_current2_title.place(x=730, y=383)
 delay_current = Text(master=window,  height=1, width=4,font=('SF Pro Display',10), bg="#f6f9fc", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
 delay_current.place(x=755, y=384)

 for c in delay_c:
  delay_current.insert(END, c)
  delay_current.config(state=DISABLED)
 window.after(2500, currDelay)

def status_Delay():
  statusDelay = open(file="/home/" + username + "/.local/share/Archmain/data/statusDelay")
  statusDelay_label = Text(master=window,  width=3, height=1,font=('SF Pro Display',10), bg="#f6f9fc", fg="orangered", borderwidth = 0, highlightthickness = 0,)
  statusDelay_label.place(x=700,  y=384)

  for info_statusDelay in statusDelay:
   statusDelay_label.insert(END, info_statusDelay )
   statusDelay_label.config(state=DISABLED)
   window.after(60000, status_Delay); 




# clear buttons
def  clear_homeCache():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("x.Horizontal.TProgressbar", foreground='x', background='#fed882', troughcolor='#ecf2f5', bordercolor='#bbccdd')
    progress=ttk.Progressbar(window,style="x.Horizontal.TProgressbar", orient=HORIZONTAL,length=200,mode='determinate')
    progress.place(x=250, y=595)
    labprogress=tk.Entry(window, width=4, font=('SF Pro Display',8), bg="#ecf2f5", fg="#666", borderwidth = 0, highlightthickness = 0)
    labprogress.insert(0," ")
    labprogress.place(x=460, y=595)
    import time
    progress['value'] = 5
    labprogress.insert(0,"5%     ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 30
    labprogress.insert(0,"30%     ")
    window.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.5)
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "rm -rf ~/.cache/*"; echo "Wait.." > /home/' + username + '/.local/share/Archmain/data/cache;')
     
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(1.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)



btn=tk.Button(window, height=0, width=8, text="Clear Cache", font=('SF Pro Display',10), bg='#fed882', fg="#555", borderwidth = 0, highlightthickness = 0, command=clear_homeCache)
btn.place(x=740, y=250)

def  OrphCache():
    
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "sudo pacman -Rns $(pacman -Qdtq)"; echo "Wait.." > /home/' + username + '/.local/share/Archmain/data/orphans; ')
    
btn=tk.Button(window, height=0, width=8, text="Clear Orph", font=('SF Pro Display',10), bg='#fed882', fg="#555", borderwidth = 0, highlightthickness = 0, command=OrphCache)
btn.place(x=740, y=280)

def  clear_pkgsCache():
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "sudo pacman -Scc"; echo "Wait.."  > /home/' + username + '/.local/share/Archmain/data/cachepacman; ')
    
btn=tk.Button(window, height=0, width=8, text="Clear Pkgs", font=('SF Pro Display',10), bg='#fed882', fg="#555", borderwidth = 0, highlightthickness = 0, command=clear_pkgsCache)
btn.place(x=740, y=310)

#-------------------------------------------------------------------------------------------------------------------------

# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Credits")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x150")
    newWindow.maxsize(200,150)
    newWindow.minsize(200,150)
    newWindow.configure(bg='#f6f9fc')

    # A Label widget to show in toplevel
    Label(newWindow, text =" ", font=('SF Pro Display', 10 ), bg="#f6f9fc", fg="#555").pack(side=TOP)
    Label(newWindow, text ="Ivan Karavitis", font=('SF Pro Display', 10 ), bg="#f6f9fc", fg="#555").pack(side=TOP)
    Label(newWindow, text ="Jonathan Sanfilippo", font=('SF Pro Display', 10 ), bg="#f6f9fc", fg="#555").pack(side=TOP)
    Label(newWindow, text =" ", font=('SF Pro Display', 10 ), bg="#f6f9fc", fg="#555").pack(side=TOP)
    Label(newWindow, text =" ", font=('SF Pro Display', 10 ), bg="#f6f9fc", fg="#555").pack(side=TOP)

btn = Button(window, text ="Credits", font=('SF Pro Display', 8), bg="#ecf2f5", fg="#0f94d2",  borderwidth = 0, highlightthickness = 0,command = openNewWindow)
btn.place(x=190, y=593)




window.after(100, status_check); 
window.after(100, status_Delay); 
window.after(100, currDelay)
window.after(100, cachePac_upd)
window.after(100, orphans_upd)
window.after(100, cache_upd)
window.after(100, ssd_upd)
window.after(100, pkgs_upd)
window.after(100,kernel_upd)
window.after(100, message_Delay)
window.after(100, last_chk) 
window.after(100, list_upd)
window.after(100, pending_upd)
window.after(100, ram_upd)
window.after(100, currServer)
window.mainloop()




