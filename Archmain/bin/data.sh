#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#Setting ------------------------------------------------------------------------
VERSION="219"
CURRENTVERSION="$HOME/.local/share/Archmain/data/currentVersion"
ICON="$HOME/.local/share/Archmain/img/logo.png" ;

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
chSet="$HOME/.local/share/Archmain/data/checkSet"



#Variable Cmd
get_Variables(){
AUR=$(pikaur -Qqua ;)
ListUpdates=$(checkupdates 2>/dev/null )
Pending=$(expr $(pikaur -Qqua | wc -l) + $(checkupdates 2>/dev/null | wc -l) )
CHECK=$( expr "$(cat $chSet)" \* 60) #loop
CheckSET=$(cat $chSet)
DELAY=$( expr "$(cat $delay)" \* 60)
NDELAY=$(cat $delay)
Version=$(wget -O $version https://raw.githubusercontent.com/JonathanSanfilippo/Archmain/main/version)
DataTime=$(date '+%a %d %b %H:%M '  )
}


while true; do
get_Variables
echo  "$Version " #only for console
echo "$USER@$HOSTNAME" > "$list"
echo '' >> "$list"
echo "$VERSION" > "$CURRENTVERSION"



#Pending
if [ "$Pending" = 0 ]; then
             echo "System Updated" > "$pending"
else
  echo "$Pending Update Pending" > "$pending"
  echo "$ListUpdates" "$AUR"  >> "$list"
   ACTION=$(notify-send -i "$ICON" --action="OPEN" --action="DELAY"  -a "Archmain" "$Pending Updates available."   -u critical;  )
                case "$ACTION" in
                      "0")
                         $py
                         
                         ;;
                      "1")
                         NEXT=$(date "+%a %d %b %H:%M"  --date="$NDELAY  minutes")
                          echo "$NEXT" > "$messageDelay"
                          echo "ON" > "$statusDelay"
                         sleep "$DELAY";
                         
                         ;;
                      
                esac
   
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
NEXT=$(date  "+%a %d %b %H:%M"  --date="$CheckSET minute")
echo "$NEXT" > "$messageDelay"
 echo "OFF" > "$statusDelay"
 

sleep "$CHECK"
get_Variables
done
