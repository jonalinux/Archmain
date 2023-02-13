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

# Remove Archmain files
rm -rf "$HOME/.config/archmain"

# Remove autostart file
rm -f "$HOME/.config/autostart/checkupdates.desktop"
rm -f "$HOME/.config/autostart/tray.desktop"

# Remove Archmain desktop file
rm -f "$HOME/.local/share/applications/archmain.desktop"

# Uninstall Python packages
sudo pip uninstall -y psutil customtkinter pillow

# Array of installed packages
installed_packages=(git pacman-contrib downgrade tk reflector python-pip jq wget syslog-ng base-devel python-pyqt5)

# Loop through the installed packages
for package in "${installed_packages[@]}"
do
  # Remove the package
  sudo pacman -Rsn --noconfirm $package
done

echo "Archmain - Arch System Management has been successfully uninstalled."
