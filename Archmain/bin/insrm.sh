#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>




#Variable URL
options=$(cat "$HOME/.local/share/Archmain/bin/xopt")
package=$(cat "$HOME/.local/share/Archmain/bin/xpkg")


sudo pikaur $options  $package

echo ""
echo ""
read -p "Press [Enter] key to Esc"
echo ""
echo ""

