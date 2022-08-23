#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>




#Variable URL
chnw="$HOME/.local/share/Archmain/bin/chnw.sh"
urltemp="$HOME/.local/share/Archmain/data/temp"



echo "Writing a log file"; 
echo $(date) > "$urltemp"
echo  "last updates" >> "$urltemp"
echo ""
checkupdates   >> "$urltemp"
sudo pacman -Syu
echo ""
echo ""
read -p "Press [Enter] key to save list updates.."
echo ""
$chnw
