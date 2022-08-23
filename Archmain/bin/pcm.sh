#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>




#Variable URL
list="$HOME/.local/share/Archmain/data/listupdates"
pending="$HOME/.local/share/Archmain/data/pending"
statusDelay="$HOME/.local/share/Archmain/data/statusDelay"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"
ini="$HOME/.local/share/Archmain/data/config/set.ini"
gr="$HOME/.local/share/Archmain/data/gr.ini"
grini="$HOME/.local/share/Archmain/data/config/gr.ini"
or="$HOME/.local/share/Archmain/data/or.ini"
orini="$HOME/.local/share/Archmain/data/config/or.ini"
config="$HOME/.local/share/Archmain/data/config"
urltemp="$HOME/.local/share/Archmain/data/temp"

T=$(cat $HOME/.local/share/Archmain/data/terminal);

echo "Writing a log file"; 
echo $(date) > "$urltemp"
echo  "last updates" >> "$urltemp"
echo ""
checkupdates   >> "$urltemp"
$T "sudo pacman -Syu";
mv "$urltemp"  "$HOME/.local/share/Archmain/data/@lastup" 



