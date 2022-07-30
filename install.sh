#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>


#colors
Color_Off='\033[0m' 
Green='\033[1;32m'
Blue='\033[1;34m'
Red='\033[1;31m'
Yellow='\033[0;33m' 


mkdir -p Archmain/data


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


echo -e ${Blue}'check for a compatible terminal..'${Color_Off}
#terminal check
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
sleep 3



#libnotify
echo -e ${Blue}'check for notify-send '${Color_Off}
sleep 3
if ! [ -x "$(command -v notify-send)" ]; then
  echo -e ${Red}Error: notify-send is not installed.${Color_Off} >&2
  echo -e ${Yellow}install notify-send..${Color_Off}
  sudo pacman -S libnotify;
  echo -e  ${Green}notify-send.. installed!${Color_Off};
  else
  echo -e  ${Green}notify-send.. installed!${Color_Off}
fi




#pacman-contrib
echo ''
sleep 3
echo -e ${Blue}'check for pacman-contrib '${Color_Off}
sleep 3
if ! [ -x "$(command -v /usr/bin/checkupdates)" ]; then        
echo -e ${Red}Error: pacman-contrib is not installed.${Color_Off} >&2
echo -e ${Yellow}install pacman-contrib..${Color_Off}
  sudo pacman -S pacman-contrib;
  echo -e  ${Green}pacman-contrib. installed!${Color_Off};
  else
  echo -e  ${Green}pacman-contrib.. installed!${Color_Off}
fi



#git
echo ''
echo -e ${Blue}'check for git '${Color_Off}
sleep 3
if ! [ -x "$(command -v git)" ]; then        
echo -e ${Red}Error: git is not installed.${Color_Off} >&2
echo -e ${Yellow}install git..${Color_Off}
  sudo pacman -S git;
  echo -e  ${Green}git. installed!${Color_Off};
  else
  echo -e  ${Green}git.. installed!${Color_Off}
fi


#AURhelper
Tx=$(cat "Archmain/data/terminal")
AURhelper=$(sudo pacman -S --needed base-devel; git clone https://aur.archlinux.org/pikaur.git; cd pikaur; makepkg -fsri);
echo ''
echo -e ${Blue}'check for pikaur '${Color_Off}
sleep 3
if ! [ -x "$(command -v /usr/bin/pikaur -Qqua 2>/dev/null)" ]; then        
echo -e ${Red}Error: pikaur is not installed.${Color_Off} >&2
echo -e ${Yellow}install pikaur..${Color_Off}
sleep 5
 if  [ -x "$(command -v gnome-terminal)" ]; then
        cmd_pikaur $AURhelpe
   else
cmd_pikaur
$Tx -e $AURhelper
fi
  echo -e  ${Green}AURhelper installed!${Color_Off};
  else
  echo -e  ${Green}AURhelper installed!${Color_Off}
fi





echo -e ${Yellow}install Python tk${Color_Off}
sudo pacman -S tk;





#configure autostart file


echo "
[Desktop Entry]
Name=data
GenericName=data
Exec=/home/$USER/.local/share/Archmain/bin/data.sh
Type=Application" > data.desktop




cp -r Archmain/fonts ~/.local/share/
cp -r Archmain ~/.local/share/

cp -r  data.desktop ~/.config/autostart/


chmod +x ~/.local/share/Archmain/bin/data.sh
chmod +x ~/.local/share/Archmain/bin/Archmain.py

echo ''
echo -e ${Green}' Archmain installed, You should reboot.'${Color_Off}
echo ''
