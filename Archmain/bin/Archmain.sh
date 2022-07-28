#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

URL="$HOME/.local/share/Archmain";
ICON="$URL/icon/logo.png" ;
CHECK="30"
DELAY="3600"
AUR=$(pikaur -Qqua | wc -l)
PCM=$(checkupdates 2>/dev/null | wc -l); 
UPDATED="System Updated."
var=$(date)
ALL=$( expr "$AUR" + "$PCM")


check() { 
    PCM=$(checkupdates 2>/dev/null | wc -l); 
    list_pacman=$(checkupdates 2>/dev/null); 
    }

while true; do 
   check
        if (( ALL > 0 )); then
                echo "$PCM Pacman updates" > "$HOME/.local/share/Archmain/bin/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/bin/listaupds"
                echo "$list_pacman" >> "$HOME/.local/share/Archmain/bin/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/bin/listaupds"
                echo "$AUR AUR updates" >> "$HOME/.local/share/Archmain/bin/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/bin/listaupds"
                echo "$list_aur" >> "$HOME/.local/share/Archmain/bin/listaupds"
                echo $var > "$HOME/.local/share/Archmain/bin/info_lastcheck"
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
                echo  $UPDATED > "$HOME/.local/share/Archmain/bin/listaupds"
                echo $var > "$HOME/.local/share/Archmain/bin/info_lastcheck"
        fi

  sleep $CHECK;

        done
      


