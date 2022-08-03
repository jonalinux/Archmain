#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 29 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

terminal="$HOME/.local/share/Archmain/data/terminal"
Terminal=$(cat $terminal)

mkdir -p "$HOME/.local/share/Archmain/update";
wget   "https://github.com/JonathanSanfilippo/Archmain/archive/refs/heads/main.zip";
unzip "$HOME/.local/share/Archmain/main.zip" -d "$HOME/.local/share/Archmain/update";
chmod +x "$HOME/.local/share/Archmain/update/Archmain-main/install.sh";

$Terminal -e $HOME/.local/share/Archmain/update/Archmain-main/install.sh

#clean update
rm -rf "$HOME/.local/share/Archmain/update";
rm -rf "$HOME/.local/share/Archmain/main.zip"
rm -rf "$HOME/.local/share/Archmain/Archmainpy.desktop"
rm -rf "$HOME/.local/share/Archmain/data.desktop"