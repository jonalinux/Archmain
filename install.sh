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



declare -A pkgs=(
  [tk]=tk
  [python-pip]=python-pip
  [pillow]=python-pillow
  [pacman-contrib]=pacman-contrib
  [pikaur]=pikaur
  [downgrade]=downgrade
  [reflector]=reflector
)

declare -A pips=(
  [customtkinter]=customtkinter
  [psutil]=psutil
)

# Function to install missing packages
install_package() {
  local pkg="$1"
  if ! pacman -Qi "$pkg" &> /dev/null; then
    echo "$pkg not found, installing..."
    sudo pacman -S "$pkg"
  else
    echo "$pkg already installed."
  fi
}

# Function to install missing python packages
install_pip_package() {
  local pkg="$1"
  if ! pip show "$pkg" &> /dev/null; then
    echo "$pkg not found, installing via pip..."
    sudo pip install "$pkg"
  else
    echo "$pkg already installed."
  fi
}

# Check and install missing packages
for pkg in "${pkgs[@]}"; do
  install_package "$pkg"
done

# Check and install missing python packages
for pkg in "${pips[@]}"; do
  install_pip_package "$pkg"
done

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