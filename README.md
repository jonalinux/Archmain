# Archmain - Arch System Management


![repository-open-graph-template](https://user-images.githubusercontent.com/103053714/216729571-1a7b7328-47bc-4aa1-a918-410354bd8b45.png)

## NEW v. 300![Screenshot from 2023-02-05 12-57-27](https://user-images.githubusercontent.com/103053714/216820952-4eb4be6e-8e87-48b8-97ac-8cbb4f027478.png)


# Archmain
Arch Linux System Management Tool

## Installation
Clone this repository:

$ git clone https://github.com/JonathanSanfilippo/Archmain.git

Enter the directory `archmain` and give permissions to execute the bash script:

- $ cd Archmain
- $ chmod +x install.sh

Finally, run the installation script:

$ ./install.sh

## Required packages
The following packages must be installed before running the installation script:
- git
- pacman-contrib
- downgrade
- tk
- reflector
- python-pip
- libnotify
- jq

## Compatible terminals
    "gnome-terminal",
    "konsole",
    "xfce4-terminal",
    "kgx",
    "lxterminal",
    "mate-terminal",
    "deepin-terminal",
    "qterminal",
    "terminator",
    "tilix",
    "terminology",
    "xterm",
    "sakura"


## Configuration
The installation script will automatically set up the configuration and create two files:
- `checkupdates.desktop` in `~/.config/autostart/` to start the checkupdates script at login.
- `archmain.desktop` in `~/.local/share/applications/` to start the `archmain` application.

The configuration directory is located at `~/.config/archmain/`.
