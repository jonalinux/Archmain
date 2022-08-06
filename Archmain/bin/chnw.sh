#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#Setting ------------------------------------------------------------------------


#Variable URL
list="$HOME/.local/share/Archmain/data/listupdates"
pending="$HOME/.local/share/Archmain/data/pending"
statusDelay="$HOME/.local/share/Archmain/data/statusDelay"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"

#Variable Cmd
get_Variables(){
ListUpdates=$(pikaur -Qu)
Pending=$(pikaur -Quq | wc -l)
DataTime=$(date '+%a %d %b %H:%M '  )
}

get_Variables
echo "$USER@$HOSTNAME" > "$list"
echo ' ' >> "$list"

#Pending
if [ "$Pending" = 1 ]; then
  echo "$Pending Update Pending" > "$pending"
  echo "$ListUpdates"  >> "$list"
  elif
   [ "$Pending" -gt 0 ]; then
  echo "$Pending Updates Pending" > "$pending"
  echo "$ListUpdates"  >> "$list"

  else
   echo "System Updated" > "$pending"
   echo ' Last Check Performed manually: System Updated' >> "$list"
fi

 echo "OFF" > "$statusDelay"
echo "$DataTime" > "$lastcheck"
