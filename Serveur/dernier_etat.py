#!/usr/bin/python

##
##Retourne une dictionnaire ayant les dernier etat de tous les machines .
##Si on pas encore recu d'information la donne est remplace "-"
##exemple : dernier_etat nom_table1 nom_table2 ...
##
##
##

import sqlite3 as lite
import sys,os

con = lite.connect("/var/GestionSysteme/service.db")
value = {}
with con:
	for table in sys.argv:	
		cur = con.cursor()		
		if table != sys.argv[0]:
			data = cur.execute("Select distinct machine from port_machine")
	
			for row in data:
				cur1 = con.cursor()	
				cur1.execute("Select  machine,date,information from "+table+ " where machine='"+row[0]+"' order by date DESC Limit 1  ") 
				donn = cur1.fetchone()
				if not len is None:
					if not value.has_key(row[0]): 
						try :
							value[row[0]] = [donn[1]]
						except :
							value[row[0]] = ['-']
					try :
						if value[row[0]][0] < donn[1]:
							value[row[0]][0] = donn[1]
					except :
						value[row[0]][0] = value[row[0]][0]
					try :
						value[row[0]].append(donn[2])   
					except :
						value[row[0]].append('-')
					cur1.close()
	
		cur.close()
print value

