#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#Setting ------------------------------------------------------------------------
VERSION="200"

ICON="$HOME/.local/share/Archmain/img/logo.png" ;

#loop
CHECK="60" #min 1m safe CPU
WAIT="300"

#py
py="$HOME/.local/share/Archmain/bin/Archmain.py"

#updateArchmain
Aupd="$HOME/.local/share/Archmain/bin/update.sh"

#Variable URL
version="$HOME/.local/share/Archmain/data/version"
log="$HOME/.local/share/Archmain/data/log"
list="$HOME/.local/share/Archmain/data/listupdates"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"
packages="$HOME/.local/share/Archmain/data/packages"
pending="$HOME/.local/share/Archmain/data/pending"
terminal="$HOME/.local/share/Archmain/data/terminal"
kernel="$HOME/.local/share/Archmain/data/kernel"
ram="$HOME/.local/share/Archmain/data/ram"
ssd="$HOME/.local/share/Archmain/data/ssd"
cache="$HOME/.local/share/Archmain/data/cache"
orphans="$HOME/.local/share/Archmain/data/orphans"
delay="$HOME/.local/share/Archmain/data/delay"

#Variable Cmd
get_Variables(){
NumberUpdates=$(pikaur -Qqua | wc -l)
ListUpdates=$(pikaur -Quq)
Log=$(pikaur -Qu)
PackagesTotal=$(pacman -Q | wc -l )
DataTime=$(date)
Pending=$(pikaur -Quq | wc -l)
Kernel=$(uname -r )
Ram=$(free -t | awk 'FNR == 2 {printf("%.2f%"), $3/$2*100}')
SSD=$(du -sh / | awk '{ printf $1}')
Cache=$( du -sh $HOME/.cache/ | awk '{ printf $1}')
Orphans=$(pacman -Qtdq | wc -l)
DELAY=$( expr "$(cat $delay)" \* 60)
Version=$(wget -O $version https://raw.githubusercontent.com/JonathanSanfilippo/Archmain/main/version)
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


while true; do
get_Variables
echo '' #only for console
echo "$USER@$HOSTNAME" > "$list"
echo '' >> "$list"


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
#lastcheck
echo "$DataTime" > "$lastcheck"
#Pending
if [ "$Pending" == 1 ]; then
  echo "$Pending Update Pending" > "$pending"
  elif
   [ "$Pending" -gt 0 ]; then
  echo "$Pending Updates Pending" > "$pending"
  else
   echo "System Updated" > "$pending"
fi


#list
#fix both in one 
if [ "$NumberUpdates" -gt 0 ]; then
  
  echo "$ListUpdates"  >> "$list"
  echo "$DataTime" > "$log"
  echo " " >> "$log"
  echo "$Log"  >> "$log"
  else
  echo ''
fi
if [ "$Pending" == 0 ]; then
  echo 'System Updated.' >> "$list"
  else
           ACTION=$(notify-send -i "$ICON" --action="OPEN" --action="DELAY"  -a "Archmain" "$Pending Updates available."   -u critical;  )
                case "$ACTION" in
                      "0")
                         $py
                         sleep $WAIT;
                         ;;
                      "1")
                         sleep $DELAY;
                         
                         ;;
                      
                esac
                
fi


#checkversion
checkVersion=$(cat $version)
if [ "$checkVersion" -gt "$VERSION" ]; then
  
ACTION=$(notify-send -i "$ICON" --action="Update"   -a "Archmain" "Archmain Update available. Version $checkVersion."   -u critical;  )
                case "$ACTION" in
                      "0")
                         $Aupd
                         sleep $WAIT;
                         ;;
                      "1")
                         
                         
                         ;;
                      
                esac
else

echo ''

fi

sleep $CHECK
get_Variables
done
