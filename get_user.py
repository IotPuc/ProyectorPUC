'''
This module gets the teacher who is using the
class room
'''

#Tomas Herrera
#PUC

from quickstart import getCalendar

from unidecode import unidecode

def getWho():
    calendar = getCalendar()
    summary = calendar[0][1]
    last_name = summary.split(" ")[-1].lower()
    print "Current User is: {}\n\n".format(last_name)
    return last_name

def getUserMACs():
    person = unidecode(getWho().decode("utf-8"))
    person = person.lower()
    print person
    MACs = []
    with open("/usr/local/sbin/database.txt","r") as f:
        line = f.readline()
        while line != "":
            if person in line:
                MACs.append(line.split(" ")[-1][0:-1])
            line = f.readline()

    return MACs


