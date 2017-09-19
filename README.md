##An IoT-Ready Streaming Manager Device for Classroom Environments in a Smart Campus

The content of this git goes into:

´´´
/usr/bin/local/sbin
´´´

In the Raspberry edit the crontab:

'''
sudo crontab -e
'''

and add:

'''
@reboot sleep 10 && /usr/local/sbin/python_launch.sh >/usr/local/sbin/logs/logfile 2>&1
@reboot python /usr/local/sbin/restartmqtt.py
'''

Install pymssql:

´´´
sudo apt-get update && sudo apt-get install freetds-dev freetds-bin && sudo apt-get install python-dev python-pip && sudo pip install pymssql
´´´

Run a SQL server on a computer in the LAN

SQL server pass> Qw2244946

To start a VNC connection initiate a VNC Server on Windows with tightvnc or in linux/mac with x11vnc.

