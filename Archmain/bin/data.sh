#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>



#Setting ------------------------------------------------------------------------
VERSION="220"
CURRENTVERSION="$HOME/.local/share/Archmain/data/currentVersion"
ICON="$HOME/.local/share/Archmain/img/logo.png" ;

#py
py="$HOME/.local/share/Archmain/bin/Archmain.py"


#Variable URL
info="$HOME/.local/share/Archmain/data/info"
version="$HOME/.local/share/Archmain/data/version"
list="$HOME/.local/share/Archmain/data/listupdates"
pending="$HOME/.local/share/Archmain/data/pending"
delay="$HOME/.local/share/Archmain/data/delay"
messageDelay="$HOME/.local/share/Archmain/data/messageDelay"
statusDelay="$HOME/.local/share/Archmain/data/statusDelay"
lastcheck="$HOME/.local/share/Archmain/data/lastcheck"
chSet="$HOME/.local/share/Archmain/data/checkSet"
terminal="$HOME/.local/share/Archmain/data/terminal"



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
Version=$(wget -O $info https://raw.githubusercontent.com/JonathanSanfilippo/Archmain/main/info)
DataTime=$(date '+%a %d %b %H:%M '  )
}


while true; do
get_Variables
echo  "$Version " #only for console
echo "$USER@$HOSTNAME" > "$list"
echo '' >> "$list"
echo "$VERSION" > "$CURRENTVERSION"



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
infomess=$(cat $info)
if [ "$checkVersion" -gt "$VERSION" ]; then
  
notify-send -i "$ICON"    -a "Archmain" "Archmain Update available." "Version $checkVersion. shorturl.at/bmXZ5.  $infomess"   -u critical;
               
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
