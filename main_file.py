#!/usr/bin/python

import subprocess as sp
from get_ip import returnAllPossibleIPs
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import datetime

def main():
        print "Entering Main Function"
        IPs = returnAllPossibleIPs()
        print "Returned IPs for user: {}\n\n".format(IPs)
        p1 = "-fullscreen"
        p2 = "-viewonly"
        p3 = "-x11cursor"
        ps = []

        # Connect to the ips
	for i in IPs:
		ip=i[0]
		print i
		time.sleep(1)
		p=sp.Popen(["/usr/bin/vncviewer", ip, p1,p2], stdout=sp.PIPE,stderr=sp.PIPE)
		time.sleep(3)
	        if "Connected to RFB server" in  p.stderr.readline():
			mqqtt="IP;{},MAC;{},USER;{}".format(i[0],i[1],i[2])
			publish.single("Proyector","[CONNECTION],"+mqqtt,hostname="localhost")
			p.wait()
			publish.single("Proyector","[DISCONNECTION],"+mqqtt,hostname="localhost")
	'''
        for i in IPs:
                ip = i[0]
                print ip
                print "Trying to connect to: {}".format(ip)
                p = sp.Popen(["/usr/bin/vncviewer", ip, p1, p2], stdout=sp.PIPE, stderr=sp.PIPE,bufsize=1)
                ps.append(p)

        IN = False
        if len(ps):
                IN = True


        while IN:
                for i in ps:
                        for com in iter(i.stderr.readline, b''):
                                print com
				if com == "": break
                                print "RETURNED: {}".format(com)
                                if "server closed connection" in com or "Unable to connect" in com:
                                        IN = False
                                i.stdout.close()

	'''
        print "FINISHED PROCEDURE"


if __name__ == "__main__":
        while True:
                main()
