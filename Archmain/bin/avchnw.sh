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
LOGFILE="$HOME/.local/share/Archmain/data/avlog"
INFO="$HOME/.local/share/Archmain/data/avinfo"
SIZE="$HOME/.local/share/Archmain/data/avsize"
ini3="$HOME/.local/share/Archmain/data/config/avset.ini"
gr="$HOME/.local/share/Archmain/data/gr.ini"
grini="$HOME/.local/share/Archmain/data/config/gr.ini"
av="$HOME/.local/share/Archmain/data/av.ini"
avini="$HOME/.local/share/Archmain/data/config/av.ini"
config="$HOME/.local/share/Archmain/data/config"
list="$HOME/.local/share/Archmain/data/listupdates"


get_Variables(){
AVset=$(cat "$HOME/.local/share/Archmain/data/avset")
DIRSIZE=$(du -sh $DIR 2>/dev/null | cut -f1);
DIR=$(cat "$HOME/.local/share/Archmain/data/avdir") #---------- "/" default set all system
}
  

get_Variables

if ! [ -x "$(command -v clamscan --help)" ]; then #------------ check if clamav is installed on your system.
      cp -r "$av" "$config"
      mv "$avini" "$ini3"
      echo "Not installed" > "$INFO"
      exit; # ------------------------------if clamav is not installed, it writes info to GUI and Closes the script.
else   
      echo "$DIRSIZE" > "$SIZE";
              if  [ "$AVset" = "000" ]; then #-----if set 000 clamav its disabled
                  cp -r "$av" "$config"
                  mv "$avini" "$ini3"
                 echo "Enable ClamAV before!!" > "$INFO"
                 echo "It looks like you are trying to start ClamAV manual scan without having it enabled in Archmain first. Simply set a time in AV Set Check to enable the script, remember to set the path to scan as well." > "$list"
            else
                # nice -n5 clamscan -ri $DIR > "$LOGFILE" 
                
                clamscan -ri $DIR > "$LOGFILE" 
                MALWARE=$(tail "$LOGFILE"|grep Infected|cut -d" " -f3);
                 cp -r "$LOGFILE" "$list"
                 if [ "$MALWARE" -eq "0" ];then
                       cp -r "$gr" "$config"
                       mv "$grini" "$ini3"
                       echo "System Protect " > "$INFO"
                       else
                       cp -r "$av" "$config"
                       mv "$avini" "$ini3"
                       echo "$MALWARE Malware detected" > "$INFO"
                            
                 fi
      
      
      fi          
fi

