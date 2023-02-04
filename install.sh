#!/bin/bash
# 
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


#colors
Color_Off='\033[0m' 
Green='\033[1;32m'
Blue='\033[1;34m'
Red='\033[1;31m'
Yellow='\033[0;33m' 


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


#git, notify-send, pacman-contrib, downgrade, tk, reflector, python-pip, python-pillow, customtkinter psutil 

sudo pikaur -S git notify-send pacman-contrib downgrade tk reflector python-pip python-pillow

pip install customtkinter
pip install psutil




# Create the $home/.config/archmain directory
config_dir="$HOME/.config/archmain"
mkdir -p "$config_dir"

# Copy all files to the $home/.config/archmain directory
cp * "$config_dir"

# Define the username variable
username=$(whoami)

# Create the checkupdates.desktop file
cat << EOF > "/home/$username/.config/autostart/checkupdates.desktop"
[Desktop Entry]
Type=Application
Exec=$config_dir/scripts/checkupdates
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=checkupdates.desktop
EOF

# Create the archmain.desktop file
cat << EOF > "/home/$username/.local/share/applications/archmain.desktop"
[Desktop Entry]
Type=Application
Name=Archmain
Icon=$config_dir/icons/app-icon.png
Exec=python3 $config_dir/archmain.py
Comment=Arch System Management
Terminal=false
Categories=Utility;
EOF


# Make all files executable
chmod +x "$config_dir"/*
chmod +x "$config_dir/scripts"/*


echo "Installation complete, it is necessary to reboot in order to launch the Archmain start scripts."
