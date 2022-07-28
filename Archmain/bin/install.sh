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



cmd_pikaur(){ pikaur=$(sudo pacman -S --needed base-devel; git clone https://aur.archlinux.org/pikaur.git; cd pikaur; makepkg -fsri);}



echo -e ${Blue}'check for a compatible terminal..'${Color_Off}

sleep 3
if  [ -x "$(command -v gnome-terminal)" ]; then
           echo -e ${Green}find gnome-terminal, passed!${Color_Off};
           echo "gnome-terminal" > "Archmain/data/terminal"
         elif  [ -x "$(command -v konsole)" ]; then
         echo -e ${Green}find konsole, passed!${Color_Off};
         echo "konsole" > "Archmain/data/terminal"
         elif  [ -x "$(command -v xfce4-terminal)" ]; then
         echo -e ${Green}find xfce4-terminal, passed${Color_Off};
         echo "xfce4-terminal" > "Archmain/data/terminal"
         elif  [ -x "$(command -v kgx)" ]; then
         echo  -e ${Green}find gnome-console, passed!${Color_Off};
         echo "kgx" > "Archmain/data/terminal"
          elif  [ -x "$(command -v lxterminal)" ]; then
         echo  -e ${Green}find lxterminal , passed!${Color_Off};
         echo "lxterminal" > "Archmain/data/terminal"
          elif  [ -x "$(command -v alacritty)" ]; then
         echo  -e ${Green}find alacritty , passed!${Color_Off};
         echo "alacritty" > "Archmain/data/terminal"
          elif  [ -x "$(command -v mate-terminal)" ]; then
         echo  -e ${Green}find mate-terminal , passed!${Color_Off};
         echo "mate-terminal" > "Archmain/data/terminal"
          elif  [ -x "$(command -v deepin-terminal)" ]; then
         echo  -e ${Green}find deepin-terminal , passed!${Color_Off};
         echo "deepin-terminal" > "Archmain/data/terminal"
          elif  [ -x "$(command -v qterminal)" ]; then
         echo  -e ${Green}find qterminal , passed!${Color_Off};
         echo "qterminal" > "Archmain/data/terminal"
          elif  [ -x "$(command -v terminator)" ]; then
         echo  -e ${Green}find terminator , passed!${Color_Off};
         echo "terminator" > "Archmain/data/terminal"
          elif  [ -x "$(command -v tilix)" ]; then
         echo  -e ${Green}find tilix , passed!${Color_Off};
         echo "tilix" > "Archmain/data/terminal"
          elif  [ -x "$(command -v xterm)" ]; then
         echo  -e ${Green}find xterm , passed!${Color_Off};
         echo "xterm" > "Archmain/data/terminal"
         else
         echo -e ${Red}you should have installed a compatible terminal: xfce4-terminal konsole gnome-terminal mate-terminal lxterminal deepin-terminal terminator qterminal alacritty tilix  xterm kitty
${Color_Off}
         fi;
echo ''

#terminal
TERMINAL=$(cat "Archmain/data/terminal")


#configure autostart file
echo "
[Desktop Entry]
Name=Archmain
GenericName=Archmain
Exec=/home/$USER/.local/share/Archmain/bin/Archmain.sh
Type=Application
Categories=GTK;GNOME;System;" > Archmain.desktop

#configure python app
echo "
[Desktop Entry]
Name=arch-find
GenericName=arch-find
Exec=/home/$USER/.local/share/Archmain/bin/Archmain.py
Type=Application
Icon=/home/$USER/.local/share/Archmain/icon/icon.png
Categories=GTK;GNOME;System;" > Archmainpy.desktop




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


echo ''
echo -e ${Blue}'check for pikaur '${Color_Off}
sleep 3
if ! [ -x "$(command -v /usr/bin/pikaur -Qqua 2>/dev/null)" ]; then        
echo -e ${Red}Error: pikaur is not installed.${Color_Off} >&2
echo -e ${Yellow}install pikaur..${Color_Off}
sleep 5
 if  [ -x "$(command -v gnome-terminal)" ]; then
        cmd_pikaur $pikaur
   else
cmd_pikaur
$TERMINAL -e $pikaur
fi
  echo -e  ${Green}pikaur. installed!${Color_Off};
  else
  echo -e  ${Green}pikaur.. installed!${Color_Off}
fi

echo -e ${Yellow}install tk${Color_Off}
sudo pacman -S tk;




cp -r Archmain/fonts ~/.local/share/
cp -r Archmain ~/.local/share/

cp -r  Archmain.desktop ~/.config/autostart/
cp -r Archmainpy.desktop ~/.local/share/applications/
chmod +x ~/.local/share/Archmain/bin/Archmain.sh
chmod +x ~/.local/share/Archmain/bin/find.sh
chmod +x ~/.local/share/Archmain/bin/aur-pacman-notify.sh
chmod +x ~/.local/share/Archmain/bin/Archmain.py

echo ''
echo -e ${Green}' Archmain installed, You should reboot.'${Color_Off}
echo ''
