#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#REFRESH GUI ------------------------------------------------------------------------

#Variable URL
packages="$HOME/.local/share/Archmain/data/packages"
terminal="$HOME/.local/share/Archmain/data/terminal"
kernel="$HOME/.local/share/Archmain/data/kernel"
ram="$HOME/.local/share/Archmain/data/ram"
ssd="$HOME/.local/share/Archmain/data/ssd"
cache="$HOME/.local/share/Archmain/data/cache"
orphans="$HOME/.local/share/Archmain/data/orphans"
cachepacman="$HOME/.local/share/Archmain/data/cachepacman"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"

#Variable Cmd
get_Variables(){
PackagesTotal=$(pacman -Q | wc -l )
Kernel=$(uname -r )
Ram=$(free -t | awk 'FNR == 2 {printf("%.2f%"), $3/$2*100}')
SSD=$(du -sh / | awk '{ printf $1}')
Cache=$( du -sh $HOME/.cache/ | awk '{ printf $1}')
Orphans=$(pacman -Qtdq | wc -l)
CachePacman=$(du -sh  /var/cache/pacman/pkg  | awk '{ printf $1}')

}

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

get_Variables

#terminal check
if  [ -x "$(command -v $T1)" ]; then
           echo "$T1  -- /bin/sh -c" > "$terminal"
elif    [ -x "$(command -v $T2)" ]; then
           echo $T2 -e  > "$terminal"
elif    [ -x "$(command -v $T3)" ]; then
           echo $T3 -e  > "$terminal"
elif    [ -x "$(command -v $T4)" ]; then
           echo $T4 -e  > "$terminal"
elif    [ -x "$(command -v $T5)" ]; then
           echo $T5 -e  > "$terminal"
elif    [ -x "$(command -v $T6)" ]; then
           echo $T6 -e  > "$terminal"
elif    [ -x "$(command -v $T7)" ]; then
           echo $T7 -e  > "$terminal"
elif    [ -x "$(command -v $T8)" ]; then
           echo $T8 -e  > "$terminal"
elif    [ -x "$(command -v $T9)" ]; then
           echo $T9 -e  > "$terminal"
elif    [ -x "$(command -v $T10)" ]; then
           echo $T10 -e  > "$terminal"
elif    [ -x "$(command -v $T11)" ]; then
           echo $T11 -e  > "$terminal"
elif    [ -x "$(command -v $T12)" ]; then
           echo $T12 -e  > "$terminal"
fi;


#Packages installed in Arch
echo "$PackagesTotal" > "$packages"
#kernel
echo "$Kernel" > "$kernel"
#ram
echo "$Ram" > "$ram"
#ssd
echo "$SSD" > "$ssd"
#cache
echo "$Cache" > "$cache"
#orphans
echo "$Orphans" > "$orphans"
#CachePackages
echo "$CachePacman" > "$cachepacman"


