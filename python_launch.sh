#!/bin/bash


export DISPLAY=:0.0
XAUTHORITY=/home/pi/.Xauthority
USER="pi"
LOGNAME=pi
DESKTOP_SESSION=LXDE-pi
HOME=/home/pi

printenv
echo $XAUTHORITY
xhost +
xauth $DISPLAY
cd /
sudo /usr/bin/python /usr/local/sbin/main_file.py > /usr/local/sbin/logs/pythonlog.log 2>&1
cd /
