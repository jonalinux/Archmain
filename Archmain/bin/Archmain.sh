#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

URL="$HOME/.local/share/Archmain";
CHECK="10"
AUR=$(pikaur -Qqua | wc -l)
PCM=$(checkupdates 2>/dev/null | wc -l); 


check_pcm() { 
    UPDATES=$(checkupdates 2>/dev/null | wc -l); 
    list_pacman=$(checkupdates 2>/dev/null); 
    }

check_aur() {
    AUR=$(pikaur -Qqua | wc -l);
    list_aur=$(pikaur -Qqua);
}


while true; do 
   check_pcm
        if (( UPDATES > 0 )); then
                echo "$PCM Pacman updates" > "$HOME/.local/share/Archmain/data/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/data/listaupds"
                echo "$list_pacman" >> "$HOME/.local/share/Archmain/data/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/data/listaupds"
                echo "$AUR AUR updates" >> "$HOME/.local/share/Archmain/data/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/data/listaupds"
                echo "$list_aur" >> "$HOME/.local/share/Archmain/data/listaupds"
                exec $URL/bin/aur-pacman-notify.sh
                
        else
                echo  $UPDATES #only for test console
        fi

     check_aur
        if (( AUR > 0 )); then
                echo "$PCM Pacman updates" > "$HOME/.local/share/Archmain/data/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/data/listaupds"
                echo "$list_pacman" >> "$HOME/.local/share/Archmain/data/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/data/listaupds"
                echo "$AUR AUR updates" >> "$HOME/.local/share/Archmain/data/listaupds"
                echo ' ' >> "$HOME/.local/share/Archmain/data/listaupds"
                echo "$list_aur" >> "$HOME/.local/share/Archmain/data/listaupds"
                $URL/bin/aur-pacman-notify.sh
        else
                echo  $AUR #only for test console
        fi

        

  sleep $CHECK;

        done
      


