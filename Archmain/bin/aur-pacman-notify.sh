#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

URL="$HOME/.local/share/Archmain";
ICON="$URL/icon/logo.png" ;
DELAY="3600"
WAITING="300" #waiting after action install 5 min.
AUR=$(pikaur -Qqua | wc -l)
PCM=$(checkupdates 2>/dev/null | wc -l); 
TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal")
ALL=$( expr "$AUR" + "$PCM")

# per python dopo!!!!!!!!!!!!!!!
#yes_action () { 
#       if  [ -x "$(command -v gnome-terminal)" ]; then
#         gnome-terminal -- /bin/bash -c 'pikaur -Sua'
   #else
#         $TERMINAL -e 'pikaur -Sua'
   #fi;
#}



  ACTION=$(notify-send -i "$ICON" --action="OPEN" --action="DELAY"  -a "Archmain" "$ALL Updates available."   -u critical;  )
                  case "$ACTION" in
                      "0")
                         exec $URL/bin/Archmain.py
                         sleep $WAITING;
                         exec $URL/bin/Archmain.sh
                         
                         ;;
                      "1")
                         sleep $DELAY;
                         exec $URL/bin/Archmain.sh
                         ;;
                      
                esac

#if you handle_dismiss (X)
sleep $DELAY;
exec $URL/bin/Archmain.sh