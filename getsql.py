import pymssql

def getUserMACsSQL():
	conn=pymssql.connect(server='lab-pc.ing.puc.cl',user='SA',password='Qw2244946',database='Proyector')
	curs=conn.cursor()

	curs.execute('SELECT * FROM vnc_data')
	usrs = []
	for row in curs:
        	usrs.append([row[1],row[0]])
	conn.close()
	
	return usrs

print getUserMACsSQL()
