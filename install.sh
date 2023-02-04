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

# Colors
Color_Off='\033[0m'
Green='\033[1;32m'
Blue='\033[1;34m'
Red='\033[1;31m'
Yellow='\033[0;33m'

#!/bin/bash

echo -e "${Blue}Checking for base-devel...${Color_Off}"

# Check if base-devel is already installed
if pacman -Q base-devel &> /dev/null; then
  echo -e "${Green}base-devel is already installed!${Color_Off}"
else
  echo -e "${Yellow}Installing base-devel...${Color_Off}"

  # Install base-devel
  sudo pacman -S base-devel

  # Confirm the installation
  if pacman -Q base-devel &> /dev/null; then
    echo -e "${Green}base-devel has been successfully installed.${Color_Off}"
  else
    echo -e "${Red}Error: Failed to install base-devel.${Color_Off}" >&2
  fi
fi

echo -e "${Blue}Checking for pikaur...${Color_Off}"

# Check if pikaur is installed
if ! command -v pikaur &>/dev/null; then
  echo -e "${Red}Error: pikaur is not installed.${Color_Off}" >&2
  echo -e "${Yellow}Installing pikaur...${Color_Off}"
  
  # Installing required dependencies
  sudo pacman -S --needed base-devel

  # Clone the pikaur repository and install it
  git clone https://aur.archlinux.org/pikaur.git
  cd pikaur
  makepkg -fsri

  # Clean up
  cd ..
  rm -rf pikaur
else
  echo -e "${Green}Pikaur is already installed!${Color_Off}"
fi

# Array of required packages
required_packages=(git pacman-contrib downgrade tk reflector python-pip libnotify)

# Function to check if a package is installed
function is_installed {
  pacman -Qi $1 &> /dev/null
  return $?
}

echo -e "${Blue}Checking for required packages...${Color_Off}"

# Loop through the required packages
for package in "${required_packages[@]}"
do
  # Check if the package is installed
  if ! is_installed $package; then
    # If not installed, install it
    sudo pikaur -S $package --noconfirm
  else
    echo -e "${Green}$package is already installed!${Color_Off}"
  fi
done

echo -e "${Blue}Installing Python packages...${Color_Off}"

# Install Python packages
pip install psutil customtkinter pillow

echo -e "${Blue}Setting up the configuration...${Color_Off}"

# Create the $HOME/.config/archmain directory
config_dir="$HOME/.config/archmain"
mkdir -p "$config_dir"
mkdir -p "$HOME/.local/share/Trash/"

# Copy all files to the $HOME/.config/archmain directory
cp -r * "$config_dir"

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
find "$config_dir" -type f -exec chmod +x {} \;

echo -e "${Red}Warning: Installation complete, but it is necessary to reboot in order to launch the Archmain start scripts. ${Color_Off}"

