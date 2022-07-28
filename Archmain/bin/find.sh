#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo 
# Date Fri Jul 22 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>

#TERMINAL=$(cat "$HOME/.local/share/Archmain/data/terminal")
INPUT=$(cat "$HOME/.local/share/Archmain/data/input")

pikaur -S $INPUT


