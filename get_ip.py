'''
This module gets the ip address from
a MAC address thats on the same
internet host
'''

#Tomas Herrera C
#PUC

from ping_all import getMACsIPs
from get_user import getUserMACs
from getsql import getUserMACsSQL

import subprocess as sp
import re

def getIP(MACs, AllMACs):
    IPs = []
    for MAC,usr in MACs:
        for Tupple in AllMACs:
            if MAC in Tupple[1]:
                IPs.append((re.search("(?<=for )\S+",Tupple[0]).group(0),MAC,usr))
    return IPs


def returnAllPossibleIPs():
    AllLocalUsers = getMACsIPs()  # pings all possible IP's
    print "Conexions to LAN: {}\n\n".format(AllLocalUsers)
    #UserMACs = getUserMACs() #decoment this line if you want calendar feature
    UserMACs = getUserMACsSQL() # [FD:61:F0:21:22, ...] , [Felipe, ..]
    print "Current User MACs: {}\n\n".format(UserMACs)
    #UserMACs = ["00:22:5F:D2:AF:1A"]
    IPs = getIP(UserMACs, AllLocalUsers)
    
    return IPs # [("ip","mac","felipe"),("ip","mac","tomas")..]
    
    
