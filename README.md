# Archmain - Arch System Management 


![repository-open-graph-template](https://user-images.githubusercontent.com/103053714/216729571-1a7b7328-47bc-4aa1-a918-410354bd8b45.png)

This is a graphical user interface (GUI) for the package manager in Arch Linux. The purpose of this GUI is to make it easier for users to manage packages on their Arch Linux system.

### Video Tutorial

[Watch video on Youtube](https://www.youtube.com/watch?v=WBTL0oi173c)




### Description


![Screenshot from 2023-02-07 15-02-23](https://user-images.githubusercontent.com/103053714/217281610-e45bd2e9-49fd-4dd2-979b-e57b60d53aa4.png)


The GUI is built using Python and the Tkinter library, and is designed to be simple and intuitive to use. The interface includes buttons for installing, removing, updating, and clearing the cache of packages. Additionally, the interface includes a label that displays the current size of the cache of packages.

The GUI uses the pikaur package manager, which is a popular AUR helper for Arch Linux. The pikaur command-line utility is used to perform the various package management tasks, and the output of these commands is displayed in a terminal window within the GUI.


![Screenshot from 2023-02-07 15-06-14](https://user-images.githubusercontent.com/103053714/217282708-5c9ae4bb-1b75-4991-8416-ae8e0793fcfb.png)


The source code is available on GitHub and can be easily modified to suit the needs of individual users. The code is well-commented and easy to understand, making it a great starting point for anyone interested in creating a similar project.

## Getting Started
Getting Started with the Arch Linux Package Manager GUI, you will need to have a working installation of Arch Linux with the Tkinter library installed. Additionally, you will need to have the pikaur package manager installed.

Once these requirements are met, simply clone the repository and run the script using Python. The GUI will launch and you can start using it to manage your packages.



![216841376-3b6b8104-a3a4-4468-8a99-2b54c5172086](https://user-images.githubusercontent.com/103053714/217284297-f7b83216-0978-4c7e-9358-b43dfe829266.png)

### Using the GUI 
The GUI is simple to use and provides a straightforward way to perform common package management tasks. To install a package, simply enter the name of the package in the text box and press the "Install" button. To remove a package, enter the name of the package in the text box and press the "Remove" button. To update all installed packages, press the "Update" button. To clear the cache of packages, press the "Clear" button. The current size of the cache of packages is displayed in a label at the bottom of the interface.


![Screenshot from 2023-02-07 15-16-27](https://user-images.githubusercontent.com/103053714/217285215-f09ef3f8-ff21-486e-a33c-a12f9eb990cb.png)



### Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Your contributions are greatly appreciated! 



# Archmain
Arch Linux System Management Tool

## Uninstall OLD VERSION < 288
- https://github.com/JonathanSanfilippo/Uninstall-Archmain-Old-version-228-.git

## Installation
Clone this repository:

$ git clone https://github.com/JonathanSanfilippo/Archmain.git

Enter the directory `archmain` and give permissions to execute the bash script:

- $ cd archmain
- $ chmod +x install.sh

Finally, run the installation script:

$ ./install.sh


## Update version

you can use update instead of install to update the version only if you are already using archmain v300+ installed on your Arch Linux.


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
- wget
- base-devel
- pikaur



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

### Contributors
- @IvanKey1

###

[![name](https://ckdcf.org/wp-content/uploads/button-donate-paypal-1-300x137.png)](https://www.paypal.com/donate/?hosted_button_id=3C4YAF9NXMEWL)









