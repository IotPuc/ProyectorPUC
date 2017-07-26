'''
This module gets the local IP
Address and pings all possible
ip's (1-255).

This is supposing that the
raspberry is connected via
'''

#Tomas Herrera C
#PUC

import subprocess as sp
import os
import re

def getLocalIP(wifi=True):
    if wifi:
        cmd = "ifconfig"
        p = sp.Popen(cmd, stdout=sp.PIPE)
        p.wait()
        output = p.communicate()[0].split("\n")
        c = 0
        for line in output:
            c += 1
            if "wlan0" in line:
                ipline = output[c]
        ip_cls = re.search("(?<=addr:)\S+", ipline)
        raspberry_ip = ip_cls.group(0)
        rasp_split = raspberry_ip.split(".")
        global_ip = ".".join(rasp_split[:-1]) + "."
        return global_ip
    return False

def getMACsIPs(wifi=True):
    global_ip = getLocalIP(wifi) + "0/24"
    p = sp.Popen(["nmap", "-sP", global_ip], stdout=sp.PIPE)
    p.wait()
    Nmap = []
    string = p.communicate()[0].split("\n")
    for line in string:
        if len(line) > 10 and ("Nmap" == line[:4] or "MAC" == line[:3]):
            Nmap.append(line)
    
    return makeTuples(Nmap[:-1])

def makeTuples(l):
    h = []
    for i in range(len(l)):
        if "Nmap" == l[i][0:4]:
            if i+1 < len(l) and l[i+1][0:3] == "MAC":
                h.append((l[i], l[i+1]))
    return h
    


