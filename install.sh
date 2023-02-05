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



#!/bin/bash

# Colors
Green='\033[1;32m'
Blue='\033[1;34m'
Red='\033[1;31m'
Yellow='\033[0;33m'
Color_Off='\033[0m'

# Required packages
required_packages=(git pacman-contrib downgrade tk reflector python-pip libnotify jq)

# Function to check if a package is installed
function is_installed {
  pacman -Qi $1 &> /dev/null
  return $?
}

echo -e "${Blue}Checking for base-devel...${Color_Off}"
if pacman -Q base-devel &> /dev/null; then
  echo -e "${Green}base-devel is already installed!${Color_Off}"
else
  echo -e "${Yellow}Installing base-devel...${Color_Off}"
  sudo pacman -S base-devel
  if pacman -Q base-devel &> /dev/null; then
    echo -e "${Green}base-devel has been successfully installed.${Color_Off}"
  else
    echo -e "${Red}Error: Failed to install base-devel.${Color_Off}"
  fi
fi

echo -e "${Blue}Checking for pikaur...${Color_Off}"
if ! command -v pikaur &>/dev/null; then
  echo -e "${Red}Error: pikaur is not installed.${Color_Off}"
  echo -e "${Yellow}Installing pikaur...${Color_Off}"
  sudo pacman -S --needed base-devel
  git clone https://aur.archlinux.org/pikaur.git
  cd pikaur
  makepkg -fsri
  cd ..
  rm -rf pikaur
else
  echo -e "${Green}Pikaur is already installed!${Color_Off}"
fi

echo -e "${Blue}Checking for required packages...${Color_Off}"
for package in "${required_packages[@]}"
do
  if ! is_installed $package; then
    sudo pikaur -S $package --noconfirm
  else
    echo -e "${Green}$package is already installed!${Color_Off}"
  fi
done

echo -e "${Blue}Installing Python packages...${Color_Off}"
pip install psutil customtkinter pillow

echo -e "${Blue}Setting up the configuration...${Color_Off}"
config_dir="$HOME/.config/archmain"
mkdir -p "$config_dir"
mkdir -p "$HOME/.local/share/Trash/"
mkdir -p "$HOME/.local/share/applications/"
mkdir -p "$HOME/.config/autostart"
cp -r * "$config_dir"

username=$(whoami)



# Create the checkupdates.desktop file
cat << EOF > "/home/$username/.config/autostart/checkupdates.desktop"
[Desktop Entry]
Type=Application
Exec=$config_dir/scripts/checkupdates
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Check Updates
Comment=Autostart script to check for updates
Icon=system-software-update
Categories=System;Utility;
StartupNotify=true
EOF

# Create the archmain.desktop file
cat << EOF > "/home/$username/.local/share/applications/archmain.desktop"
[Desktop Entry]
Type=Application
Name=Archmain
Icon=/home/jonathan/.config/archmain/icons/app-icon.png
Exec=python3 /home/jonathan/.config/archmain/archmain.py
Comment=Arch System Management
Terminal=false
Categories=System;
StartupNotify=true
StartupWMClass=Archmain
EOF

# Make all files executable
chmod +x "/home/$username/.config/archmain/scripts/*"
chmod +x "/home/$username/.config/archmain/*"


echo -e "${Green}Installation complete!${Color_Off}"
echo -e "${Yellow}Reboot now!${Color_Off}"
