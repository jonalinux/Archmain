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
window.geometry("1280x800+10+20")
window.maxsize(1280, 800)
window.minsize(1280, 800)
window.configure(bg='#202124')
username = getpass.getuser()
p1 = PhotoImage(file="/home/" + username + "/.local/share/Archmain/icon/icon2.png")
window.iconphoto(False, p1)   

 
#top 
image = tk.PhotoImage(file="/home/" + username + "/.local/share/Archmain/img/logo.png")
banner = tk.Frame(master=window, height=80, bg="#303134") 
banner.pack(fill=tk.X)
linebanner = tk.Frame(master=window, width=900 ,height=5, bg="#0f94d2")
linebanner.place(x=265, y=60)
canvas = Canvas(width = 90, height = 80, bg="#303134", borderwidth = 0, highlightthickness = 0)
canvas.create_image(50, 40, image = image)
canvas.place(x=0, y=0)
title = tk.Label(master=window, text="Archmain", font=('SF Pro Display', 25, 'bold'), bg="#303134", fg="#fff")
title.place(x=90, y=12)
subtitle = tk.Label(master=window, text="Archlinux Manager GUI", font=('SF Pro Display',11), bg="#303134", fg="#0f94d2")
subtitle.place(x=90, y=50)
version = tk.Label(master=window, text="Version", font=('SF Pro Display',10), bg="#303134", fg="#FFF")
version.place(x=1180, y=50)
numversion = Text(window, width=6, height=1, font=('SF Pro Display',11), bg="#303134", fg="#0f94d2", borderwidth = 0, highlightthickness = 0)
numversion.place(x=1230, y=50)

sidebar = tk.Frame(master=window, width=360, height=700, bg="#232429", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
sidebar.place(x=0, y=120)
menu = tk.Frame(master=window, width=1280, height=50, bg="#303134", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
menu.place(x=0, y=75)
 
#footer
footer2 = tk.Frame(master=window, width=980, height=50, bg="#232429", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
footer2.place(x=360, y=722)
footer = tk.Frame(master=window, width=1280, height=30, bg="#232429", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
footer.place(x=0, y=772)
author = tk.Label(master=window, text="© 2022 Jonathan Sanfilippo, Ivan Karavitis. ", font=('SF Pro Display',9), bg="#232429", fg="#B6B6B7")
author.place(x=1035, y=776)


def wiki(url):
    webbrowser.open_new(url)
 
wiki = Button(window, text ="  Wiki", cursor="hand2", font=('SF Pro Display', 10), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#B0B3B8",  borderwidth = 0, highlightthickness = 0)
wiki.place(x=0, y=770)
wiki.bind("<Button-1>", lambda e: callback("https://github.com/JonathanSanfilippo/Archmain/wiki")) 



github = open(file="/home/" + username + "/.local/share/Archmain/data/currentVersion")
for ver in github:
   numversion.insert(END, ver )
numversion.config(state=DISABLED)





def callback(url):
    webbrowser.open_new(url)
    
link1 = Label(window, text="", font=('SF Pro Display',20), bg="#303134", activebackground="#303134", activeforeground="#25db51", fg="#F5F5F7", borderwidth = 0, highlightthickness = 0, cursor="hand2")
link1.place(x=1200, y=10)
link1.bind("<Button-1>", lambda e: callback("https://github.com/JonathanSanfilippo/Archmain"))   




#progressbar


s = ttk.Style()
s.theme_use('clam')
s.configure("x.Horizontal.TProgressbar", foreground='#232429', background='#25db51', troughcolor='#202124', bordercolor='#202124')
progress_bk = tk.Frame(master=window, width=250, height=0, bg="#202124", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
progress_bk.place(x=371, y=700)
progress=ttk.Progressbar(window,style="x.Horizontal.TProgressbar", orient=HORIZONTAL,length=800,mode='determinate')
progress.place(x=365, y=700)
progress_bk = tk.Frame(master=window, width=800, height=4, bg="#202124", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
progress_bk.place(x=365, y=712)
progress_bk = tk.Frame(master=window, width=800, height=4, bg="#202124", highlightthickness=0,highlightbackground = "#0f94d2", highlightcolor= "#0f94d2")
progress_bk.place(x=365, y=700)
labprogress=tk.Entry(window, width=4, font=('SF Pro Display',11), bg="#202124", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0)
labprogress.insert(0," ")
labprogress.place(x=1200, y=698)





#--------------- Console 
 
def list_upd(): 
 #background_lista = tk.Frame(master=window, width=588, height=500, bg="#303134")
 #background_lista.place(x=15, y=130,)
 #background_lista.config( highlightthickness=0,highlightbackground = "#bbccdd", highlightcolor= "#bbccdd")
 content = open(file="/home/" + username + "/.local/share/Archmain/data/listupdates")
 lista=Text(master=window,  width=80, height=28,font=('Source Code Pro',11), bg='#202124', fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, )
 lista.place(x=425, y=160,)

 for updates in content:
   lista.insert(END, updates )
 lista.config(state=DISABLED) 
 window.after(5000, list_upd)



# --------------------------- Sidebar GUI

def kernel_upd():
 krn="Kernel=$(uname -r ); kernel=$HOME/.local/share/Archmain/data/kernel ;"
 os.system( krn + '  echo $Kernel > $kernel')
 kernel = open(file="/home/" + username + "/.local/share/Archmain/data/kernel")
 kernel_label_title = tk.Label(master=window, text="Kernel:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 kernel_label_title.place(x=40, y=160)
 kernel_label = Text(master=window,  width=14, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 kernel_label.place(x=95, y=161)

 for info_kernel in kernel:
   kernel_label.insert(END, info_kernel )
 kernel_label.config(state=DISABLED)
 window.after(60000,kernel_upd)


def pending_upd():
 colors = open(file="/home/" + username + "/.local/share/Archmain/data/config/set.ini") 
 pending = open(file="/home/" + username + "/.local/share/Archmain/data/pending")
 pending_label_title = tk.Label(master=window, text="Status:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 pending_label_title.place(x=40, y=190)
 pending_label = Text(master=window,  width=19, height=1,font=('SF Pro Display',12), bg="#232429", borderwidth = 0, highlightthickness = 0,)
 pending_label.place(x=95, y=191)
 
 for cx in colors:
  pending_label.config(fg=cx)
 
 for info_pending in pending:
   pending_label.insert(END, info_pending )
 pending_label.config(state=DISABLED)
 window.after(5000, pending_upd)
 

 
def Check_now():
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
    
btn=tk.Button(window, cursor="hand2", height=1, width=2, text="",  font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#25db51", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=Check_now)
btn.place(x=6, y=188)
 
  
def pkgs_upd():
 pax="PackagesTotal=$(pacman -Q | wc -l ); packages=$HOME/.local/share/Archmain/data/packages ; "
 os.system( pax + '  echo "$PackagesTotal" > "$packages"')
 pkgs_count = open(file="/home/" + username + "/.local/share/Archmain/data/packages")
 pkgs_count_label_title = tk.Label(master=window, text="Packages:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 pkgs_count_label_title.place(x=40, y=220)
 pkgs_count_label = Text(master=window,  width=4, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 pkgs_count_label.place(x=115, y=221)

 for info_pkgs_count in pkgs_count:
   pkgs_count_label.insert(END, info_pkgs_count )
 pkgs_count_label.config(state=DISABLED)
 window.after(5000, pkgs_upd)
 
 
def ram_upd(): 
 ramy=" RM=$HOME/.local/share/Archmain/data/ram  ; "
 ramx="Ram=$(free -h | grep G | awk -F" + "'i       '"  +  " '{ print $2 }');"   
 os.system( ramx + ramy +   ' echo "$Ram" > "$RM"'  )
 ram = open(file="/home/" + username + "/.local/share/Archmain/data/ram")
 ram_label_title = tk.Label(master=window, text="Memory usage:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 ram_label_title.place(x=40, y=251)
 ram_label = Text(master=window,  width=5, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 ram_label.place(x=150, y=252)

 for info_ram in ram:
   ram_label.insert(END, info_ram )
   ram_label.config(state=DISABLED)
 window.after(5000, ram_upd)

def ssd_upd():
 ssdx="SSD=$(df -h / | grep G|awk '{printf $3}')"
 os.system( ssdx + " ssd=$HOME/.local/share/Archmain/data/ssd;   echo  $SSD > $ssd")
 ssd = open(file="/home/" + username + "/.local/share/Archmain/data/ssd")
 ssd_label_title = tk.Label(master=window, text="Disc usage:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 ssd_label_title.place(x=40, y=281)
 ssd_label = Text(master=window,  width=10, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 ssd_label.place(x=124, y=282)

 for info_ssd in ssd:
   ssd_label.insert(END, info_ssd )
 ssd_label.config(state=DISABLED)
 window.after(5000, ssd_upd)
 
 
def cache_upd():
 chx="Cache=$( du -sh $HOME/.cache/ | awk '{ printf $1}'); cache=$HOME/.local/share/Archmain/data/cache ;"
 os.system( chx + ' echo "$Cache" > "$cache"')
 cache = open(file="/home/" + username + "/.local/share/Archmain/data/cache")
 cache_label_title = tk.Label(master=window, text="Cache:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 cache_label_title.place(x=40, y=311)
 cache_label = Text(master=window,  width=5, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 cache_label.place(x=95, y=312)

 for info_cache in cache: 
   cache_label.insert(END, info_cache )
 cache_label.config(state=DISABLED)
 window.after(5000, cache_upd)


# clear buttons
def  clear_homeCache():
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
     
btn=tk.Button(window, cursor="hand2", height=0, width=2, text="", font=('SF Pro Display',11),bg="#232429", activebackground="#232429", activeforeground="#f3425f", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=clear_homeCache)
btn.place(x=6, y=309)

 

def orphans_upd():
 orph="Orphans=$(pacman -Qtdq | wc -l); orphans=$HOME/.local/share/Archmain/data/orphans ;"
 os.system( orph + ' echo "$Orphans" > "$orphans"')
 orphans = open(file="/home/" + username + "/.local/share/Archmain/data/orphans")
 orphans_label_title = tk.Label(master=window, text="Orphans:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 orphans_label_title.place(x=40, y=341)
 orphans_label = Text(master=window,  width=4, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 orphans_label.place(x=110, y=342)

 for info_orphans in orphans:
   orphans_label.insert(END, info_orphans )
 orphans_label.config(state=DISABLED)
 window.after(5000, orphans_upd)


def  OrphCache():
    
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "sudo pacman -Rns $(pacman -Qdtq)"; echo "Wait.." > /home/' + username + '/.local/share/Archmain/data/orphans; ')
    
btn=tk.Button(window, cursor="hand2", height=0, width=2, text="", font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#f3425f", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=OrphCache)
btn.place(x=6, y=339)
 

def cachePac_upd():
 cpax="CachePacman=$(du -sh  /var/cache/pacman/pkg  | awk '{ printf $1}');  cachepacman=$HOME/.local/share/Archmain/data/cachepacman ;"
 os.system( cpax + '  echo "$CachePacman" > "$cachepacman"')
 cachePacman = open(file="/home/" + username + "/.local/share/Archmain/data/cachepacman")
 cachePacman_label_title = tk.Label(master=window, text="Packages Cache:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 cachePacman_label_title.place(x=40, y=371)
 cachePacman_label = Text(master=window,  width=5, height=1,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 cachePacman_label.place(x=165, y=372)

 for info_cachePacman in cachePacman:
   cachePacman_label.insert(END, info_cachePacman )
 cachePacman_label.config(state=DISABLED)
 window.after(5000, cachePac_upd)
 
 
def  clear_pkgsCache():
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal"); $TERMINAL "sudo pacman -Scc"; echo "Wait.."  > /home/' + username + '/.local/share/Archmain/data/cachepacman; ')
    
btn=tk.Button(window, cursor="hand2", height=0, width=2, text="", font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#f3425f", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=clear_pkgsCache)
btn.place(x=6, y=369)
 
 
 # bottom mirrorlist •
def mirrorlist():
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

btn=tk.Button(window, cursor="hand2", height=1, width=2, text="", font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=mirrorlist)
btn.place(x=6, y=396,)
server=Label(window, height=1, text="Rank Server Mirrors:", font=('SF Pro Display',12), bg='#232429', fg="#999", borderwidth = 0, highlightthickness = 0)
server.place(x=40, y=399,)

 

def currServer():
 server_c=open(file="/home/" + username + "/.local/share/Archmain/data/server")   
 server_current = Text(master=window,  height=1, width=4,font=('SF Pro Display',12), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
 server_current.place(x=180, y=400)

 for S in server_c:
  server_current.insert(END, S)
  server_current.config(state=DISABLED)
 window.after(5000, currServer)


 #Reflector mirrors
def reflector():
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


country=Entry(window,  width=4,font=('SF Pro Display',12), bg="#303134", fg="#FFF",borderwidth = 0, highlightthickness = 0, insertbackground="#0f94d2")
country.place(x=120, y=429,)
country.insert(0, " gb")
btn=tk.Button(window, cursor="hand2", height=1, width=2, text="", font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=reflector).place(x=6, y=426,)
labelrf=Label(window, height=1, text="Reflector *", font=('SF Pro Display',12), bg='#232429', fg="#999", borderwidth = 0, highlightthickness = 0)
labelrf.place(x=40, y=429,)
#info=Label(window, font=('SF Pro Display',9), bg='#232429', fg="#888", text="*Select the HTTP / HTTPS mirrors synchronized in the last 12 hours \n and located according  to the chosen country and overwrite \n the /etc/pacman.d/mirrorlist file with the results.")
#info.place(x=5, y=640,)
 
 
 
 #set check
def checkSet_set():
    import time
    progress['value'] = 15
    labprogress.insert(0,"15%     ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 40
    labprogress.insert(0,"40%     ")
    window.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.1)
    result=checkSet_label.get() 
    os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/checkSet;")
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)
    
checkSet=open(file="/home/" + username + "/.local/share/Archmain/data/checkSet")    
btnSet=tk.Button(window, cursor="hand2", height=1, width=2, text="",font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=lambda:[checkSet_set()])
btnSet.place(x=6, y=457)
checkSet_label_title = tk.Label(master=window, text="Set Check Updates", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
checkSet_label_title.place(x=40, y=459)
checkSet_label = Entry(master=window,  width=4,font=('SF Pro Display',12), bg="#303134", fg="#FFF", borderwidth = 0, highlightthickness = 0,insertbackground="#0f94d2" )
checkSet_label.place(x=180, y=460)
checkSet_label.insert(0, "60")



def status_check():
  statuscheck = open(file="/home/" + username + "/.local/share/Archmain/data/checkSet")
  statuscheck_label = Text(master=window,  height=1, width=4,font=('SF Pro Display',10), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
  statuscheck_label.place(x=255,  y=464)
  statuscheck_title = tk.Label(master=window, text="Min", font=('SF Pro Display',10), bg="#232429", fg="#b0b3b8")
  statuscheck_title.place(x=230, y=463)


  for info_statuscheck in statuscheck:
   statuscheck_label.insert(END, info_statuscheck )
   statuscheck_label.config(state=DISABLED)
   window.after(2500, status_check); 


#delay
def delay_set():
    import time
    progress['value'] = 15
    labprogress.insert(0,"15%     ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 40
    labprogress.insert(0,"40%     ")
    window.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 65
    labprogress.insert(0,"65%      ")
    window.update_idletasks()
    time.sleep(0.1)
    result=checkSet_label.get() 
    result=delay_label.get() 
    os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/delay;")
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)
    
delay=open(file="/home/" + username + "/.local/share/Archmain/data/delay")    
btnSet2=tk.Button(window, cursor="hand2", height=1, width=2, text="", font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#b0b3b8",borderwidth = 0, highlightthickness = 0, command=delay_set)
btnSet2.place(x=6, y=487)
delay_label_title = tk.Label(master=window, text="Set Check Delay", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
delay_label_title.place(x=40, y=489)
delay_label = Entry(master=window,  width=4,font=('SF Pro Display',12), bg="#303134", fg="#FFF", borderwidth = 0, highlightthickness = 0,insertbackground="#0f94d2")
delay_label.place(x=180, y=490)
delay_label.insert(0, "120")


   
def currDelay():
 delay_c=open(file="/home/" + username + "/.local/share/Archmain/data/delay")   
 delay_current2_title = tk.Label(master=window, text="Min", font=('SF Pro Display',10), bg="#232429", fg="#b0b3b8")
 delay_current2_title.place(x=230, y=492)
 delay_current = Text(master=window,  height=1, width=4,font=('SF Pro Display',10), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
 delay_current.place(x=255, y=493)

 for c in delay_c:
  delay_current.insert(END, c)
  delay_current.config(state=DISABLED)
 window.after(2500, currDelay)

def status_Delay():
  statusDelay = open(file="/home/" + username + "/.local/share/Archmain/data/statusDelay")
  statusDelay_label = Text(master=window,  width=3, height=1,font=('SF Pro Display',10), bg="#232429", fg="orangered", borderwidth = 0, highlightthickness = 0,)
  statusDelay_label.place(x=290,  y=494)

  for info_statusDelay in statusDelay:
   statusDelay_label.insert(END, info_statusDelay )
   statusDelay_label.config(state=DISABLED)
   window.after(60000, status_Delay); 
 
 
 
 # -------------------------- Rollback 
 
def rollback_set():
 result=rollback_label.get() 
 os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");    $TERMINAL "sudo downgrade '+ result + ' "' )

rollback_label = Entry(master=window,  width=20,font=('SF Pro Display',12), bg="#303134", fg="#FFF", borderwidth = 0, highlightthickness = 0,insertbackground="#0f94d2")
rollback_label.insert(0, ' PackageName')
rollback_label.place(x=110, y=522,)
btn=tk.Button(window, cursor="hand2", height=1, width=2, text="",  font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="orange", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=rollback_set)
btn.place(x=6, y=520,)
rb_label_title = tk.Label(master=window, text="Rollback", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
rb_label_title.place(x=40, y=522)

 

#@lastup
def log():
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


btnInstall=tk.Button(window, cursor="hand2", height=1, width=2, text="",font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="orange", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=log)
btnInstall.place(x=6, y=551)
rb_label_title = tk.Label(master=window, text="Last installed Updates", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
rb_label_title.place(x=40, y=552)

# bottom install only pacman 
def install_pac():
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");    $TERMINAL /home/' + username + '/.local/share/Archmain/bin/pcm.sh')
   
  
btnInstall=tk.Button(window, cursor="hand2", height=1, width=2, text="", font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="magenta", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=install_pac)
btnInstall.place(x=6, y=581,)
pcm_label_title = tk.Label(master=window, text="Exclude AUR Updates", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
pcm_label_title.place(x=40, y=582)



def avinfo():
 colors = open(file="/home/" + username + "/.local/share/Archmain/data/config/avset.ini") 
 pending = open(file="/home/" + username + "/.local/share/Archmain/data/avinfo")
 pending_label_title = tk.Label(master=window, text="ClamAV:", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
 pending_label_title.place(x=40, y=612)
 pending_label = Text(master=window,  width=22, height=1,font=('SF Pro Display',12), bg="#232429", borderwidth = 0, highlightthickness = 0,)
 pending_label.place(x=105, y=613)
 
 for cav in colors:
  pending_label.config(fg=cav)
 
 for info_pending in pending:
   pending_label.insert(END, info_pending )
 pending_label.config(state=DISABLED)
 window.after(5000, avinfo)

def av_Check_now():
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
  
    os.system('/home/' + username + '/.local/share/Archmain/bin/avchnw.sh')

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
    
btn=tk.Button(window, cursor="hand2", height=1, width=2, text="",  font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#25db51", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=av_Check_now)
btn.place(x=6, y=611)




def av_set():
    import time
    progress['value'] = 15
    labprogress.insert(0,"15%     ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 45
    labprogress.insert(0,"45%     ")
    window.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 75
    labprogress.insert(0,"75%      ")
    window.update_idletasks()
    time.sleep(0.1)
    result=avst_label.get() 
    os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/avset;")
    os.system('/home/' + username + '/.local/share/Archmain/bin/avSetUp.sh')
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)
    
avsttt =open(file="/home/" + username + "/.local/share/Archmain/data/avset")    
btnSet3=tk.Button(window, cursor="hand2", height=1, width=2, text="",font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=lambda:[av_set()])
btnSet3.place(x=6, y=641)
avst_label_title = tk.Label(master=window, text="AV Set Check", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
avst_label_title.place(x=40, y=642)
avst_label = Entry(master=window,  width=3,font=('SF Pro Display',12), bg="#303134", fg="#FFF", borderwidth = 0, highlightthickness = 0,insertbackground="#0f94d2" )
avst_label.place(x=145, y=643)
avst_label.insert(0, "000")



def av_set_status():
  avst = open(file="/home/" + username + "/.local/share/Archmain/data/avCurrentSet")
  avst_label = Text(master=window,  height=1, width=20,font=('SF Pro Display',10), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
  avst_label.place(x=180,  y=645)
  
  for avsetx in avst:
   avst_label.insert(END, avsetx )
   avst_label.config(state=DISABLED)
   window.after(2500, av_set_status); 


def av_dirset():
    import time
    progress['value'] = 15
    labprogress.insert(0,"15%     ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 45
    labprogress.insert(0,"45%     ")
    window.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 75
    labprogress.insert(0,"75%      ")
    window.update_idletasks()
    time.sleep(0.1)
    result=avdr_label.get() 
    os.system("echo '"+ result +"' > " + " /home/" + username + "/.local/share/Archmain/data/avdir")
    os.system('/home/' + username + '/.local/share/Archmain/bin/avSetUp.sh')
    progress['value'] = 95
    labprogress.insert(0,"95%      ")
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    labprogress.insert(0,"100%      ")
    window.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 0
    labprogress.insert(0,"                        ")
    window.update_idletasks()
    time.sleep(0.1)
    
avdrrr =open(file="/home/" + username + "/.local/share/Archmain/data/avdir")    
btnSet2=tk.Button(window, cursor="hand2", height=1, width=2, text="",font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="#0f94d2", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=lambda:[av_dirset()])
btnSet2.place(x=6, y=671)
avdr_label_title = tk.Label(master=window, text="AV Dir to scan", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
avdr_label_title.place(x=40, y=672)
avdr_label = Entry(master=window,  width=6,font=('SF Pro Display',12), bg="#303134", fg="#FFF", borderwidth = 0, highlightthickness = 0,insertbackground="#0f94d2" )
avdr_label.place(x=145, y=673)
avdr_label.insert(0, " /")



def av_dirset_status():
  avdr = open(file="/home/" + username + "/.local/share/Archmain/data/avdir")
  avdr_label = Text(master=window,  height=1, width=15,font=('SF Pro Display',10), bg="#232429", fg="#0f94d2", borderwidth = 0, highlightthickness = 0, )
  avdr_label.place(x=220,  y=675)
 
  for avdrx in avdr:
   avdr_label.insert(END, avdrx )
   avdr_label.config(state=DISABLED)
   window.after(2500, av_dirset_status); 



def avlog():
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
    
    os.system('cp  /home/' + username + '/.local/share/Archmain/data/avlog  /home/' + username + '/.local/share/Archmain/data/listupdates; ')

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


btn=tk.Button(window, cursor="hand2", height=1, width=2, text="",font=('SF Pro Display',11), bg="#232429", activebackground="#232429", activeforeground="orange", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0, command=avlog)
btn.place(x=6, y=701)
avlog_label_title = tk.Label(master=window, text="Last Clamscan log", font=('SF Pro Display',12), bg="#232429", fg="#b0b3b8")
avlog_label_title.place(x=40, y=702)




 
 
 
 # ------------------------------------------------------------------------- top header
 

user = open(file="/home/" + username + "/.local/share/Archmain/data/usr")
tx_user = Text(master=window, width=20, height=1, font=('SF Pro Display',12), bg="#303134", fg="#b0b3b8", borderwidth = 0, highlightthickness = 0,)
tx_user.place(x=20, y=94)
 
for usr in user:
  tx_user.insert(END, usr )
  tx_user.config(state=DISABLED)
 
 
 
def last_chk():
 lastcheck = open(file="/home/" + username + "/.local/share/Archmain/data/lastcheck")
 label=tk.Label(window, text="  Last check: ",font=('SF Pro Display',12), fg="#b0b3b8", bg='#303134').place(x=235, y=92,)
 lastcheck_label = Text(master=window,  width=14, height=1,font=('SF Pro Display',12), bg="#303134", fg="#0f94d2", borderwidth = 0, highlightthickness = 0,)
 lastcheck_label.place(x=345, y=93)

 for info_lastcheck in lastcheck:
  lastcheck_label.insert(END, info_lastcheck )
  lastcheck_label.config(state=DISABLED)
 window.after(5000, last_chk); 
 
 
def message_Delay():
 messageDelay = open(file="/home/" + username + "/.local/share/Archmain/data/messageDelay")
 messageDelay_label_title = tk.Label(master=window, text="  Next: ", font=('SF Pro Display',12), bg="#303134", fg="#b0b3b8")
 messageDelay_label_title.place(x=505, y=92)
 messageDelay_label = Text(master=window,  width=14, height=1,font=('SF Pro Display',12), bg="#303134", fg="orange", borderwidth = 0, highlightthickness = 0,)
 messageDelay_label.place(x=570, y=93)

 for info_messageDelay in messageDelay:
  messageDelay_label.insert(END, info_messageDelay )
  messageDelay_label.config(state=DISABLED)
 window.after(5000, message_Delay); 


#------------ Install or remove Packages:

def InsRmv(): 
    package=form.get()
    option=options.get()
    os.system("echo '"+ package +"' > " + " /home/" + username + "/.local/share/Archmain/bin/xpkg")
    os.system("echo '"+ option +"' > " + " /home/" + username + "/.local/share/Archmain/bin/xopt")
    os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");    $TERMINAL /home/' + username + '/.local/share/Archmain/bin/insrm.sh')
   

options = tk.Entry(window, width=6, borderwidth = 0, highlightthickness = 0, bg="#404144", fg='#FFF', font=('SF Pro Display',12), insertbackground='#0f94d2' )
options.place(x=730, y=96)
options.insert(0," -S") 
form = tk.Entry(window, width=24, borderwidth = 0, highlightthickness = 0, bg="#404144", fg='#FFF', font=('SF Pro Display',12), insertbackground='#0f94d2' )
form.place(x=798, y=96)
form.insert(0," PackageName") 
form_title = tk.Label(master=window, text="Install or Remove AUR & Pacman packages", font=('SF Pro Display',10), bg="#303134", fg="#B6B6B7")
form_title.place(x=730, y=72)
btnPkgs=tk.Button(window, cursor="hand2", height=1, width=3, text="Run", bg='#0f94d2' , fg="#FFF", font=('SF Pro Display',10), borderwidth = 0, highlightthickness = 0, command=InsRmv)
btnPkgs.place(x=1045, y=92)




# bottom install updates
def install_Updates():
  ignore=formex.get()
  os.system("echo '"+ ignore +"' > " + " /home/" + username + "/.local/share/Archmain/bin/ignore")
  os.system('TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal");    $TERMINAL /home/' + username + '/.local/share/Archmain/bin/aur.sh')
  
formex = tk.Entry(window, width=70, borderwidth = 0, highlightthickness = 0, bg="#303134", fg='#FFF', font=('SF Pro Display',12), insertbackground='#0f94d2' )
formex.place(x=558, y=730)
formex.insert(0," --ignore Packages") 
formex_title = tk.Label(master=window, text="Exclude Packages from Update", font=('SF Pro Display',10), bg="#232429", fg="#B6B6B7")
formex_title.place(x=365, y=730)


def color_btn():  
  colors = open(file="/home/" + username + "/.local/share/Archmain/data/config/set2.ini")
  btnInstall=tk.Button(window, height=1, width=10, text="Update Now  ", font=('SF Pro Display',12), bg="#303134", activebackground="#303134", activeforeground="#25db51", borderwidth = 0, highlightthickness = 0, cursor="hand2", command=install_Updates)
  btnInstall.place(x=1135, y=92,)
  
  
  for cx2 in colors:
   btnInstall.config(fg=cx2, activeforeground=cx2)
  window.after(5000, color_btn); 



# # function to open a new window
# # on a button click
# def openNewWindow():
     
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(window)
 
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("Archmain man")
 
#     # sets the geometry of toplevel
#     newWindow.geometry("600x800")
#     newWindow.maxsize(600,800)
#     newWindow.minsize(600,800)
#     newWindow.configure(bg='#232429')

#     # A Label widget to show in toplevel
  






 



window.after(100, av_dirset_status); 
window.after(100, av_set_status); 
window.after(100, avinfo)
window.after(100, color_btn); 
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





