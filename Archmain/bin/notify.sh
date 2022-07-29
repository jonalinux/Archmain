#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

URL="$HOME/.local/share/Archmain";
ICON="$URL/icon/logo.png" ;
CHECK="60"
DELAY="3600"


check() { PCM=$(checkupdates 2>/dev/null | wc -l); AUR=$(pikaur -Qqua | wc -l); ALL=$( expr "$AUR" + "$PCM");}

while true; do 
   check
        if [ $ALL -gt 0 ]; then
                 
                 ACTION=$(notify-send -i "$ICON" --action="OPEN" --action="DELAY"  -a "Archmain" "$ALL Updates available."   -u critical;  )
                  case "$ACTION" in
                      "0")
                         
                $URL/bin/Archmain.py 
               
                         
                         ;;
                      "1")
                         sleep $DELAY;
                         
                         ;;
                      
                esac
                
        else
                echo ''
        fi

  sleep $CHECK;

        done
      


