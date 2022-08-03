# Archmain
Archmain - AUR and Pacman updater 
- Gnome
- Cinnamon
- KDE
- Deepin
- Xfce4

![Screenshot from 2022-08-03 06-36-44](https://user-images.githubusercontent.com/103053714/182532085-f42c3ad8-ad62-4647-aa59-f73731a30900.png)
![Screenshot from 2022-07-31 11-36-58](https://user-images.githubusercontent.com/103053714/182023382-9a34f3f1-1b44-4fe9-95d7-4dc6f4cf81dc.png)

Archmain
I made a small script for notifying pacman and AUR package updates, as well as the ability to easily install packages from both AUR and other GUI.
GUI interface in python and script engine in shell to have little load on memory and processor, only about 500kb.

It does not need widgets or extensions for this useful for those who want to keep a light system without too many things added, but enjoy the utility to update them and install packages easily.

The installation script installs the folder in ./local/share
and adds to autostart the script base data.sh which periodically checks for updates and writes the information to be transmitted to the gui and eventually to libnotify to notify the presence of new updates. Install the .desktop file for the python application, and check the necessary dependencies as well as install an AUR helper for managing these packages.

It is possible from the notification to use "Delay" to delay the control and update notifications to the next time, by default it is set to 1 hour, however in the gui it is possible to choose the time to be set for the "Delay" option.


- git clone https://github.com/JonathanSanfilippo/Archmain.git
- cd Archmain-main
- chmod +x ./install.sh
- ./install.sh

## Dependencies
1. libnotify
2. pacman-contrib
3. git
4. pikaur
5. tk
6. base-devel
7. wget
