#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#Setting ------------------------------------------------------------------------

#loop
CHECK="30"

#Variable URL
list="$HOME/.local/share/Archmain/data/listupdates"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"
packages="$HOME/.local/share/Archmain/data/packages"
pending="$HOME/.local/share/Archmain/data/pending"
terminal="$HOME/.local/share/Archmain/data/terminal"


#Reset data
echo "" > "$list"
echo "" > "$lastcheck"
echo "" > "$packages"
echo "" > "$pending"
echo "" > "$terminal"


#Variable Cmd
NumberUpdatesPacman=$(checkupdates 2>/dev/null | wc -l)
NumberUpdatesAUR=$(pikaur -Qqua | wc -l)
ListUpdatesPacman=$(checkupdates 2>/dev/null)
ListUpdatesAUR=$(pikaur -Qqua | wc -l)
PackagesTotal=$(pacman -Q | wc -l )
DataTime=$(date)
Pending=$( expr $(checkupdates 2>/dev/null | wc -l) + $(pikaur -Qqua | wc -l))


#Terminal check list
T1="gnome-terminal"
T2="konsole"
T3="xfce4-terminal"
T4="kgx"
T5="lxterminal"
T6="alacritty"
T7="mate-terminal"
T8="deepin-terminal"
T9="qterminal"
T10="terminator"
T11="tilix"
T12="xterm"

#---------------------------------------------------------------------------------

#Start!
while true; do

#list
if [ "$NumberUpdatesPacman" -gt 0 ]; then
  echo "$NumberUpdatesPacman Pacman updates" >> "$list"
  echo '' >> "$list"
  echo "$ListUpdatesPacman" >> "$list"
  else
  echo ''
fi
if [ "$NumberUpdatesAUR" -gt 0 ]; then
  echo "$NumberUpdatesAUR AUR updates" >> "$list"
  echo '' >> "$list"
  echo "$ListUpdatesAUR" >> "$list"
  else
  echo ''
fi

#lastcheck
echo "$DataTime" > "$lastcheck"

#Pending
if [ "$Pending" -gt 0 ]; then
  echo "$Pending Updates Pending" > "$pending"
  else
   echo "System Updated" > "$pending"
fi

#terminal check
if  [ -x "$(command -v $T1)" ]; then
           echo $T1 > "$terminal"
elif    [ -x "$(command -v $T2)" ]; then
           echo $T2 > "$terminal"
elif    [ -x "$(command -v $T3)" ]; then
           echo $T3 > "$terminal"
elif    [ -x "$(command -v $T4)" ]; then
           echo $T4 > "$terminal"
elif    [ -x "$(command -v $T5)" ]; then
           echo $T5 > "$terminal"
elif    [ -x "$(command -v $T6)" ]; then
           echo $T6 > "$terminal"
elif    [ -x "$(command -v $T7)" ]; then
           echo $T7 > "$terminal"
elif    [ -x "$(command -v $T8)" ]; then
           echo $T8 > "$terminal"
elif    [ -x "$(command -v $T9)" ]; then
           echo $T9 > "$terminal"
elif    [ -x "$(command -v $T10)" ]; then
           echo $T10 > "$terminal"
elif    [ -x "$(command -v $T11)" ]; then
           echo $T11 > "$terminal"
elif    [ -x "$(command -v $T12)" ]; then
           echo $T12 > "$terminal"
fi;
           


#Packages installed in Arch
echo "$PackagesTotal" > "$packages"





sleep $CHECK
done