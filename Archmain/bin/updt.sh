#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

ICON="$HOME/.local/share/Archmain/img/logo.png"
updt="https://github.com/JonathanSanfilippo/Archmain/archive/refs/heads/main.zip"
url="main.zip"
temp="$HOME/temp"
zip="$HOME/main.zip"
bin="$HOME/temp/Archmain-main/Archmain/bin"
data="$HOME/temp/Archmain-main/Archmain/data"
des="$HOME/.local/share/Archmain/"
version="$HOME/.local/share/Archmain/data/version"
nv=$(cat $version)

echo ""
echo "Download Update.."
wget -o -q "$url" "$updt"
echo ""

echo "Extract update"
mkdir -p "$temp"
unzip "$zip" -d "$temp"
echo ""

echo "Updating new version... $nv"
mv "$zip" "$temp"
cp -r "$bin" "$des"
chmod +x ~/.local/share/Archmain/bin/insrm.sh 
chmod +x ~/.local/share/Archmain/bin/updt.sh 
chmod +x ~/.local/share/Archmain/bin/av.sh 
chmod +x ~/.local/share/Archmain/bin/avchnw.sh 
chmod +x ~/.local/share/Archmain/bin/avSetUp.sh 
chmod +x ~/.local/share/Archmain/bin/aur.sh 
chmod +x ~/.local/share/Archmain/bin/pcm.sh    
chmod +x ~/.local/share/Archmain/bin/data.sh 
chmod +x ~/.local/share/Archmain/bin/chnw.sh  
chmod +x ~/.local/share/Archmain/bin/Archmain.py
echo ""

echo "Cleaning file..."
rm -rf "$temp"


ACTION=$(notify-send -i "$ICON" --action="Reboot now"   -a "Archmain" "update finished reboot the system now."   -u critical;  )
                case "$ACTION" in
                      "0")
                         reboot
                         ;;
                      
                esac


read -p "Press [Enter] key to finish update, and reboot your System!"
echo ""
