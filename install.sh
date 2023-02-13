#!/bin/bash
# 
#
# Author: Jonathan Sanfilippo
# Program: Archmain - Arch System Management
# Date: Feb 1 2023 - Birmingham, United Kingdom. 
# Copyright (C) 2023 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>
#
#Licenses:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Colors
Green='\033[1;32m'
Blue='\033[1;34m'
Red='\033[1;31m'
Yellow='\033[0;33m'
Color_Off='\033[0m'

v="(cat $HOME/.config/archmain/version)"
v2="(cat ./version)"


echo -e "${Blue}Check if a previous version exists.. ${Color_Off}"
sleep 5
if [ -d ~/.config/archmain/ ]; then
  
# Packages to check
PACKAGESX=(git base-devel)

# Get a list of installed packages
INSTALLED=$(pacman -Qqe)

# Iterate through the list of packages
for package in "${PACKAGESX[@]}"; do
  if echo "$INSTALLED" | grep -qw "$package"; then
    echo -e "${Green}$package is installed${Color_Off}"
  else
    echo -e "${Red}$package is NOT installed${Color_Off}"
  fi
done



# List of packages to check
PACKAGES=(git pacman-contrib downgrade tk reflector python-pip jq wget syslog-ng base-devel pikaur)
# Package to check
PACKAGE=notify-send
# Get a list of installed packages
INSTALLED=$(pacman -Qqe)

# Iterate through the list of packages
for package in "${PACKAGES[@]}"; do
  if echo "$INSTALLED" | grep -qw "$package"; then
    echo -e "${Green}$package is installed${Color_Off}"
  else
    echo -e "${Red}$package is NOT installed${Color_Off}"
    echo "Installing $package..."
    sudo pikaur -Sy "$package"
  fi
done

# List of packages to check
PACKAGES2=(psutil customtkinter pillow)

# Iterate through the list of packages
for package in "${PACKAGES2[@]}"; do
  if pip show "$package" &> /dev/null; then
    echo -e "${Green}$package is installed${Color_Off}"
  else
    echo -e "${Red}$package is NOT installed${Color_Off}"
    echo "Installing $package..."
    pip install "$package"
  fi
done


# Check if package is installed
if which "$PACKAGE" &> /dev/null; then
  echo -e "${Green}libnotify is installed${Color_Off}"
else
  echo -e "${Red}libnotify is NOT installed${Color_Off}"
  echo "Installing $PACKAGE..."
  sudo pikaur -Sy "$PACKAGE"
fi
  sleep 5
  echo -e "${Blue}Previous version $v detected, replacing the version with $v2. ${Color_Off}"
  
  config_dir="$HOME/.config/archmain"

  rm -rf "$config_dir/{data,scripts,archmain.py,version}"
  mv "$config_dir/config" "$config_dir/config.bak"
  mkdir -p "$config_dir"
  mkdir -p "$HOME/.local/share/Trash/"
  mkdir -p "$HOME/.local/share/applications/"
  mkdir -p "$HOME/.config/autostart"
  cp -r * "$config_dir"
  cp -r "$config_dir/config.bak" "$config_dir/config"
  rm -r "$config_dir/config.bak"











else
  
# Packages to check
PACKAGESX=(git base-devel)

# Get a list of installed packages
INSTALLED=$(pacman -Qqe)

# Iterate through the list of packages
for package in "${PACKAGESX[@]}"; do
  if echo "$INSTALLED" | grep -qw "$package"; then
    echo -e "${Green}$package is installed${Color_Off}"
  else
    echo -e "${Red}$package is NOT installed${Color_Off}"
  fi
done



# Package to check
PACKAGEpika=pikaur

# Get a list of installed packages
INSTALLED=$(pacman -Qqe)

# Check if package is installed
if echo "$INSTALLED" | grep -qw "$PACKAGEpika"; then
  echo -e "${Green}$PACKAGEpika is installed${Color_Off}"
else
  echo -e "${Red}$PACKAGEpika is NOT installed${Color_Off}"
  sudo pacman -S --needed base-devel git
  git clone https://aur.archlinux.org/pikaur.git
  cd pikaur
  makepkg -fsri
  cd ..
fi


# List of packages to check
PACKAGES=(git pacman-contrib downgrade tk reflector python-pip jq wget syslog-ng base-devel)
# Package to check
PACKAGE=notify-send
# Get a list of installed packages
INSTALLED=$(pacman -Qqe)

# Iterate through the list of packages
for package in "${PACKAGES[@]}"; do
  if echo "$INSTALLED" | grep -qw "$package"; then
    echo -e "${Green}$package is installed${Color_Off}"
  else
    echo -e "${Red}$package is NOT installed${Color_Off}"
    echo "Installing $package..."
    sudo pikaur -Sy "$package"
  fi
done

# List of packages to check
PACKAGES2=(psutil customtkinter pillow)

# Iterate through the list of packages
for package in "${PACKAGES2[@]}"; do
  if pip show "$package" &> /dev/null; then
    echo -e "${Green}$package is installed${Color_Off}"
  else
    echo -e "${Red}$package is NOT installed${Color_Off}"
    echo "Installing $package..."
    pip install "$package"
  fi
done


# Check if package is installed
if which "$PACKAGE" &> /dev/null; then
  echo -e "${Green}libnotify is installed${Color_Off}"
else
  echo -e "${Red}libnotify is NOT installed${Color_Off}"
  echo "Installing $PACKAGE..."
  sudo pikaur -Sy "$PACKAGE"
fi


config_dir="$HOME/.config/archmain"
mkdir -p "$config_dir"
mkdir -p "$HOME/.local/share/Trash/"
mkdir -p "$HOME/.local/share/applications/"
mkdir -p "$HOME/.config/autostart"
cp -r * "$config_dir"



# Create the checkupdates.desktop file
cat << EOF > "$HOME/.config/autostart/checkupdates.desktop"
[Desktop Entry]
Type=Application
Exec=$config_dir/scripts/checkupdates
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Check Updates
Comment=Autostart script to check for updates
Icon=system-software-update
Categories=System;Utility;
StartupNotify=true
EOF

# Create the archmain.desktop file
cat << EOF > "$HOME/.local/share/applications/archmain.desktop"
[Desktop Entry]
Type=Application
Name=Archmain
Icon=/home/$USER/.config/archmain/icons/app-icon.png
Exec=python3 /home/$USER/.config/archmain/archmain.py
Comment=Arch System Management
Terminal=false
Categories=System;
StartupNotify=true
StartupWMClass=Archmain
EOF

sudo systemctl enable syslog-ng@default.service --now
sudo systemctl start  syslog-ng@default.service


fi


# Make all files executable
find "$HOME/.config/archmain" -type f -exec chmod +x {} \;
find "$HOME/.config/archmain/scripts" -type f -exec chmod +x {} \;

echo -e "${Green}Installation complete!${Color_Off}"
echo -e "${Yellow}Reboot now!${Color_Off}"
