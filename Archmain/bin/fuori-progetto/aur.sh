#!/bin/sh
# arch-main. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 22 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>


URL="$HOME/.local/share/arch-main";
ICON="$URL/icon/update.svg" ;
DELAY="3600"
WAITING="300" #waiting after action install 5 min.
LIST=$(pikaur -Qqua 2>/dev/null);
AUR=$(pikaur -Qqua | wc -l)
TERMINAL=$(cat "$HOME/.local/share/arch-main/data/terminal")


yes_action () { 
   if  [ -x "$(command -v gnome-terminal)" ]; then
         gnome-terminal -- /bin/bash -c 'pikaur -Sua'
   else
         $TERMINAL -e 'pikaur -Sua'
   fi;
}



  ACTION=$(notify-send -i "$ICON" --action="INSTALL" --action="DELAY"  -a "arch-main" "$AUR AUR Updates available." "$LIST"  -u critical;  )
                  case "$ACTION" in
                      "0")
                         yes_action
                         sleep $WAITING;
                         exec $URL/bin/arch-main.sh
                         
                         ;;
                      "1")
                         sleep $DELAY;
                         exec $URL/bin/arch-main.sh
                         ;;
                      
                esac

#if you handle_dismiss (X)
sleep $DELAY;
exec $URL/bin/arch-main.sh
