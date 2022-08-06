#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo Ivan Karavitis 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>


#colors
Color_Off='\033[0m' 
Green='\033[1;32m'
Blue='\033[1;34m'
Red='\033[1;31m'
Yellow='\033[0;33m' 

mkdir -p ~/.local/share/applications 
mkdir -p Archmain/data
mkdir -p ~/.config/autostart
echo "60" > Archmain/data/delay

#terminal url
terminal="Archmain/data/terminal"

#Terminal check list
T1="gnome-terminal"
T2="konsole"
T3="xfce4-terminal"
T4="kgx"
T5="lxterminal"
T6="alacritty"
T7="mate-terminal"
T8="deepin-terminal"
T9="qterminal"
T10="terminator"
T11="tilix"
T12="xterm"





#terminal check----------------------------------------------------------------------------

echo -e ${Blue}'check for a compatible terminal..'${Color_Off}

if  [ -x "$(command -v $T1)" ]; then
           echo $T1 > "$terminal"
elif    [ -x "$(command -v $T2)" ]; then
           echo $T2 > "$terminal"
elif    [ -x "$(command -v $T3)" ]; then
           echo $T3 > "$terminal"
elif    [ -x "$(command -v $T4)" ]; then
           echo $T4 > "$terminal"
elif    [ -x "$(command -v $T5)" ]; then
           echo $T5 > "$terminal"
elif    [ -x "$(command -v $T6)" ]; then
           echo $T6 > "$terminal"
elif    [ -x "$(command -v $T7)" ]; then
           echo $T7 > "$terminal"
elif    [ -x "$(command -v $T8)" ]; then
           echo $T8 > "$terminal"
elif    [ -x "$(command -v $T9)" ]; then
           echo $T9 > "$terminal"
elif    [ -x "$(command -v $T10)" ]; then
           echo $T10 > "$terminal"
elif    [ -x "$(command -v $T11)" ]; then
           echo $T11 > "$terminal"
elif    [ -x "$(command -v $T12)" ]; then
           echo $T12 > "$terminal"
fi;

Tx=$(cat "Archmain/data/terminal")
  echo -e  ${Green}Teminal $Tx find ${Color_Off}
echo ' '

#libnotify-----------------------------------------------------------------------------------
echo -e ${Blue}'check for notify-send '${Color_Off}

if ! [ -x "$(command -v notify-send)" ]; then
  echo -e ${Red}Error: notify-send is not installed.${Color_Off} >&2
  echo -e ${Yellow}install notify-send..${Color_Off}
  sudo pacman -S libnotify;
  echo -e  ${Green}notify-send.. installed!${Color_Off};
  else
  echo -e  ${Green}notify-send.. installed!${Color_Off}
fi




#pacman-contrib----------------------------------------------------------------------------
echo ''
echo -e ${Blue}'check for pacman-contrib '${Color_Off}

if ! [ -x "$(command -v /usr/bin/checkupdates)" ]; then        
echo -e ${Red}Error: pacman-contrib is not installed.${Color_Off} >&2
echo -e ${Yellow}install pacman-contrib..${Color_Off}
  sudo pacman -S pacman-contrib;
  echo -e  ${Green}pacman-contrib. installed!${Color_Off};
  else
  echo -e  ${Green}pacman-contrib.. installed!${Color_Off}
fi



#git-----------------------------------------------------------------------------------------
echo ''
echo -e ${Blue}'check for git '${Color_Off}
if ! [ -x "$(command -v git)" ]; then        
echo -e ${Red}Error: git is not installed.${Color_Off} >&2
echo -e ${Yellow}install git..${Color_Off}
  sudo pacman -S git;
  echo -e  ${Green}git. installed!${Color_Off};
  else
  echo -e  ${Green}git.. installed!${Color_Off}
fi


#AURhelper check --------------------------------------------------------------------------
echo ''
echo -e ${Blue}'check for pikaur '${Color_Off}

if ! [ -x "$(command -v /usr/bin/pikaur -Qqua 2>/dev/null)" ]; then        
echo -e ${Red}Error: pikaur is not installed.${Color_Off} >&2
echo -e ${Yellow}install pikaur..${Color_Off}
AURhelper=$(sudo pacman -S --needed base-devel; git clone https://aur.archlinux.org/pikaur.git; cd pikaur; makepkg -fsri);
 if  [ -x "$(command -v gnome-terminal)" ]; then
       $Tx -c    $AURhelpe
   else
$Tx -e $AURhelper
fi
  echo -e  ${Green}AURhelper installed!${Color_Off};
  else
  echo -e  ${Green}AURhelper installed!${Color_Off}
fi



#Downgrade check ------------------------------------------------------------------
echo ''
echo -e ${Blue}'check for downgrade '${Color_Off}

if ! [ -x "$(command -v /usr/bin/downgrade --help 2>/dev/null)" ]; then        
echo -e ${Red}Error: downgrade is not installed.${Color_Off} >&2
echo -e ${Yellow}install downgrade..${Color_Off}
dw=$( git clone https://aur.archlinux.org/downgrade.git; cd downgrade; makepkg -fsri);
 if  [ -x "$(command -v gnome-terminal)" ]; then
        $Tx -c $dw
   else
$Tx -e $dw
fi
  echo -e  ${Green}downgrade installed!${Color_Off};
  else
  echo -e  ${Green}downgrade installed!${Color_Off}
fi


#wget check---------------------------------------------------------------------------------
echo ''
echo -e ${Blue}'check for wget'${Color_Off}

if ! [ -x "$(command -v wget --help)" ]; then        
echo -e ${Red}Error: wget is not installed.${Color_Off} >&2
echo -e ${Yellow}install wget${Color_Off}
  sudo pacman -S wget
  echo -e  ${Green}wget installed!${Color_Off};
  else
  echo -e  ${Green}wget installed!${Color_Off}
fi


#tk------------------------------------------------------------------------------------------

echo ''
echo -e ${Blue}'check for tkinter'${Color_Off}

if ! [ -x "$(command -v python -m tkinter)" ]; then        
echo -e ${Red}Error: tkinter is not installed.${Color_Off} >&2
echo -e ${Yellow}install tkinter${Color_Off}
  sudo pacman -S tk
  echo -e  ${Green}tkinter installed!${Color_Off};
  else
  echo -e  ${Green}tkinter installed!${Color_Off}
fi







#configure autostart file-----------------------------------------------------------------


echo "
[Desktop Entry]
Name=data
GenericName=data
Exec=/home/$USER/.local/share/Archmain/bin/data.sh
Type=Application" > data.desktop

#configure python app
echo "
[Desktop Entry]
Name=Archmain
GenericName=Archmain
Exec=/home/$USER/.local/share/Archmain/bin/Archmain.py
Type=Application
Icon=/home/$USER/.local/share/Archmain/icon/icon.png
Categories=GTK;GNOME;System;" > Archmainpy.desktop



cp -r Archmain/fonts ~/.local/share/
cp -r Archmain ~/.local/share/

cp -r  data.desktop ~/.config/autostart/
cp -r Archmainpy.desktop ~/.local/share/applications/

chmod +x ~/.local/share/Archmain/bin/data.sh     #check in loop 
chmod +x ~/.local/share/Archmain/bin/chnw.sh  #check now button script
chmod +x ~/.local/share/Archmain/bin/refresh.sh #gui refresh
chmod +x ~/.local/share/Archmain/bin/Archmain.py #gui


echo ''
echo -e ${Green}' Archmain installed, You should reboot.'${Color_Off}
echo ''
