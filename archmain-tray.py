#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QCursor
import getpass
import time
from PyQt5.QtCore import QTimer

username = getpass.getuser()
file_path = "/home/" + username + "/.config/archmain/data/tray.json"

def read_number_from_file(file_path):
    with open(file_path, "r") as f:
        return int(f.read().strip())

current_number = None

def update_icon_and_menu(tray_icon, number_action, menu):
    global current_number
    number = read_number_from_file(file_path)
    if number != current_number:
        current_number = number
        number_action.setText("Updates: {}".format(number))
        if number > 0:
            tray_icon.setIcon(QIcon("/home/" + username + "/.config/archmain/icons/tray-1.png"))
        else:
            tray_icon.setIcon(QIcon("/home/" + username + "/.config/archmain/icons/tray-0.png"))



def main():
    app = QApplication(sys.argv)

    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon("/home/" + username + "/.config/archmain/icons/tray-0.png"))

    menu = QMenu()
    menu.setStyleSheet("background-color: #202124; color: #f2f2f2; height:60px;")


    number_action = QAction("Updates: {}".format(read_number_from_file(file_path)))
    menu.addAction(number_action)

    open_action = QAction("Open")
    open_action.triggered.connect(lambda: subprocess.call(["python3", "/home/" + username + "/.config/archmain/archmain.py"]))
    menu.addAction(open_action)

    tray_icon.setContextMenu(menu)

    tray_icon.show()

    tray_icon.activated.connect(lambda reason: subprocess.call(["python3", "/home/" + username + "/.config/archmain/archmain.py"]) if reason == QSystemTrayIcon.Trigger else None)

     
    timer = QTimer()
    timer.timeout.connect(lambda: update_icon_and_menu(tray_icon, number_action, menu))
    timer.start(5000)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
