#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#Setting ------------------------------------------------------------------------
VERSION="216"
CURRENTVERSION="$HOME/.local/share/Archmain/data/currentVersion"
ICON="$HOME/.local/share/Archmain/img/logo.png" ;

#loop
CHECK="900" #min 1m safe CPU


#py
py="$HOME/.local/share/Archmain/bin/Archmain.py"


#Variable URL
version="$HOME/.local/share/Archmain/data/version"
list="$HOME/.local/share/Archmain/data/listupdates"
pending="$HOME/.local/share/Archmain/data/pending"
delay="$HOME/.local/share/Archmain/data/delay"
messageDelay="$HOME/.local/share/Archmain/data/messageDelay"
statusDelay="$HOME/.local/share/Archmain/data/statusDelay"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"


#Variable Cmd
get_Variables(){
ListUpdates=$(pikaur -Qu)
Pending=$(pikaur -Quq | wc -l)
DELAY=$( expr "$(cat $delay)" \* 60)
CHECK_conv=$( expr $CHECK / 60)
Version=$(wget -O $version https://raw.githubusercontent.com/JonathanSanfilippo/Archmain/main/version)
messDelay=$(cat $delay)
DataTime=$(date '+%a %d %b %H:%M '  )
}


while true; do
get_Variables
echo  "$Version " #only for console
echo "$USER@$HOSTNAME" > "$list"
echo '' >> "$list"
echo "$VERSION" > "$CURRENTVERSION"



#Pending
if [ "$Pending" = 1 ]; then
  echo "$Pending Update Pending" > "$pending"
  echo "$ListUpdates"  >> "$list"
   ACTION=$(notify-send -i "$ICON" --action="OPEN" --action="DELAY"  -a "Archmain" "$Pending Update available."   -u critical;  )
                case "$ACTION" in
                      "0")
                         $py
                         
                         ;;
                      "1")
                         echo "$messDelay" > "$messageDelay"
                          echo "ON" > "$statusDelay"
                         sleep "$DELAY";
                         
                         ;;
                      
                esac
  elif
   [ "$Pending" -gt 0 ]; then
  echo "$Pending Updates Pending" > "$pending"
  echo "$ListUpdates"  >> "$list"
   ACTION=$(notify-send -i "$ICON" --action="OPEN" --action="DELAY"  -a "Archmain" "$Pending Updates available."   -u critical;  )
                case "$ACTION" in
                      "0")
                         $py
                         
                         ;;
                      "1")
                         echo "$messDelay"  > "$messageDelay"
                         echo "ON" > "$statusDelay"
                         sleep "$DELAY";
                         
                         ;;
                      
                esac
  else
   echo "System Updated" > "$pending"
fi


#checkversion
checkVersion=$(cat $version)
if [ "$checkVersion" -gt "$VERSION" ]; then
  
notify-send -i "$ICON"    -a "Archmain" "Archmain Update available." "Version $checkVersion. shorturl.at/bmXZ5"   -u critical;
               
else

echo ''

fi
#lastcheck
echo "$DataTime" > "$lastcheck"
echo " $CHECK_conv" > "$messageDelay"
 echo "OFF" > "$statusDelay"
sleep $CHECK
get_Variables
done
