#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Wed Aug 24 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

#url
INFO="$HOME/.local/share/Archmain/data/avinfo"
ini3="$HOME/.local/share/Archmain/data/config/avset.ini"
gr="$HOME/.local/share/Archmain/data/gr.ini"
grini="$HOME/.local/share/Archmain/data/config/gr.ini"
av="$HOME/.local/share/Archmain/data/av.ini"
avini="$HOME/.local/share/Archmain/data/config/av.ini"
config="$HOME/.local/share/Archmain/data/config"
avCS="$HOME/.local/share/Archmain/data/avCurrentSet"


get_Variables(){
AVset=$(cat "$HOME/.local/share/Archmain/data/avset")
}
  

get_Variables

if ! [ -x "$(command -v clamscan --help)" ]; then #------------ check if clamav is installed on your system.
      cp -r "$av" "$config"
      mv "$avini" "$ini3"
      echo "Not installed" > "$INFO"
      exit; # ------------------------------if clamav is not installed, it writes info to GUI and Closes the loop.
else   
      if  [ "$AVset" = "000" ]; then #-----if set 000 clamav its disabled
           cp -r "$av" "$config"
           mv "$avini" "$ini3"
           echo "Disabled" > "$INFO"
           echo "(000=Disabled)(15=15:00)" > "$avCS"
      else
           cp -r "$gr" "$config"
           mv "$grini" "$ini3"
           echo "Enable for $AVset:00 everyday" > "$INFO"
           echo "$AVset:00" > "$avCS"
      
      fi          
fi
 