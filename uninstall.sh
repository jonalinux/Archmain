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

# Remove checkupdates.desktop file
rm -f "$HOME/.config/autostart/checkupdates.desktop"

# Remove archmain.desktop file
rm -f "$HOME/.local/share/applications/archmain.desktop"

# Remove archmain config directory
rm -rf "$HOME/.config/archmain"

# Uninstall packages
for pkg in "${pkgs[@]}"; do
  sudo pacman -R "$pkg"
done

# Uninstall pip packages
for pkg in "${pips[@]}"; do
  sudo pip uninstall "$pkg"
done

echo "Uninstallation complete."
