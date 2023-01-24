#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>
 #   This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
 #   the Free Software Foundation, either version 3 of the License, or
 #   (at your option) any later version.

 #   This program is distributed in the hope that it will be useful,
 #   but WITHOUT ANY WARRANTY; without even the implied warranty of
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.

 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <https://www.gnu.org/licenses/>.



#Variable URL
chnw="$HOME/.local/share/Archmain/bin/chnw.sh"
urltemp="$HOME/.local/share/Archmain/data/temp"
ignore=$(cat "$HOME/.local/share/Archmain/bin/ignore")


echo "Writing a log file"; 
echo "$(date)" > "$urltemp"
echo  "last updates" >> "$urltemp"
echo ""
checkupdates   >> "$urltemp"

sudo pikaur -Syu $ignore

echo ""
echo ""
read -p "Press [Enter] key to save list updates.."
echo ""
echo ""
$chnw



