#!/usr/bin/python
import sqlite3 as lite
import sys,os
##
##Recupere les port dans la base de donnee et appelle un autre programme qui gere
## l'ecoute des port
##
##
con = lite.connect("/var/GestionSysteme/service.db")
value = {}
with con:
	cur = con.cursor()		
	donnee = []	
	data = cur.execute("Select * from port_machine")
	for row in data:
		print row
		donnee.append(row[0])		
		#os.popen('ouvrir_un_port.sh '+row[0]+' &')
	cur.close()
donnee = " ".join(donnee)
print donnee
os.system("ouvrir_des_ports.sh " + donnee) # Ouverture de ports
