#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 28 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>


Fonts=" $HOME/.local/share/fonts/SF-Pro-Display-Medium.otf "
Archmain="$HOME/.local/share/Archmain"
Autostart="$HOME/.config/autostart/data.desktop "
py=" $HOME/.local/share/applications/Archmainpy.desktop"


echo ' Uninstall Archmain' 
echo ''
echo 'Remove Fonts SF-Pro-Display-Medium.otf '
rm -rf  "$Fonts"
echo 'Remove Archmain Folder in ~/.local/share/ '
rm -rf "$Archmain"
echo 'Remove Autostart and GUI app'
rm -rf "$Autostart"
rm -rf "$py"
echo 'Kill all process'
killall data.sh;

echo ' Unistall Complete need to restart'

