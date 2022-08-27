#!/bin/sh
# Archmain. maintenance app for Arch Linux.
# Author Jonathan Sanfilippo, Ivan Karavitis 
# Date Wed Aug 24 2022
# Copyright (C) 2022 Jonathan Sanfilippo <jonathansanfilippo.uk@gmail.com>


# The nice levels go from -20 to 19.

# -20 is the lowest nice level, which gives it the highest priority. 
# 19 is the highest nice level, which gives it the lowest priority. Just think of the nice level as 
# "The ability of the program to play nice with other programs." The higher the nice level, the more the program will get out of the way of other programs. 
# The lower the nice level, the more it will stop other programs from using system resources.

# The scheduling class. 0 for none, 1 for real time, 2 for best-effort, 3 for idle.

# Idle
# A program running with idle io priority will only get disk time when no other 
# program has asked for disk io for a defined grace period. The impact of idle io 
# processes on normal system activity should be zero. This scheduling class does not take a priority argument. 




#url
ICON="$HOME/.local/share/Archmain/img/logo.png"
LOGFILE="$HOME/.local/share/Archmain/data/avlog"
INFO="$HOME/.local/share/Archmain/data/avinfo"
#SIZE="$HOME/.local/share/Archmain/data/avsize"
py="$HOME/.local/share/Archmain/bin/Archmain.py"
ini3="$HOME/.local/share/Archmain/data/config/avset.ini"
gr="$HOME/.local/share/Archmain/data/gr.ini"
grini="$HOME/.local/share/Archmain/data/config/gr.ini"
av="$HOME/.local/share/Archmain/data/av.ini"
avini="$HOME/.local/share/Archmain/data/config/av.ini"
config="$HOME/.local/share/Archmain/data/config"
#list="$HOME/.local/share/Archmain/data/listupdates"


get_Variables(){
TIME=$(date +%H)
data=$(date +%d)
dailylog=$(tail "$LOGFILE"|grep "Start Date:"|cut -d":" -f4);
AVset=$(cat "$HOME/.local/share/Archmain/data/avset")
x="$data $AVset"
DIR=$(cat "$HOME/.local/share/Archmain/data/avdir") #---------- "/" default set all system
}
  
while true; do
get_Variables

if ! [ -x "$(command -v clamscan --help)" ]; then #------------ check if clamav is installed on your system.
      cp -r "$av" "$config"
      mv "$avini" "$ini3"
      echo "Not installed" > "$INFO"
      exit; # ------------------------------if clamav is not installed, it writes info to GUI and Closes the loop.
else   
      
      if [ "$TIME" -eq "$AVset" ]; then #---------if clamav is installed on the system, check if it is the correct time to perform the scan.
            if [ "$x" = "$dailylog" ]; then
                echo "nothing"
            else 
                  nice -n19 clamscan -ri $DIR > "$LOGFILE";
                  MALWARE=$(tail "$LOGFILE"|grep Infected|cut -d" " -f3);
                 if [ "$MALWARE" -eq "0" ];then
                       cp -r "$gr" "$config"
                       mv "$grini" "$ini3"
                       echo "System Protect " > "$INFO"
                       notify-send -i "$ICON"  -a "Archmain"  "System Protect "   -u critical;
                       else
                       cp -r "$av" "$config"
                       mv "$avini" "$ini3"
                       echo "$MALWARE Malware detected" > "$INFO"
                       ACTION=$(notify-send -i "$ICON" --action="OPEN" -a "Archmain"  "$MALWARE Malware detected"   -u critical;  )
                             case "$ACTION" in
                                "0")
                                $py
                                ;;
                             esac
                 fi                 
            fi
      elif  [ "$AVset" = "000" ]; then #-----if set 000 clamav its disabled
           cp -r "$av" "$config"
           mv "$avini" "$ini3"
           echo "Disabled" > "$INFO"
      
      fi          
fi
sleep 1860 #------------- loop of the script every 31 min, important to center the time selected for the control, 
           #              without repeating a scan twice at the same time set.
get_Variables           
done
