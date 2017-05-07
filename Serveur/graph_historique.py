#!/usr/bin/python
import sqlite3 as lite
import sys,os
import pygal
##
##
##Programme permetant de recuperer les donnees de tous les machines d'une table donnee
##
##exemple : graphe_historique.py nom_de_la_table
##

con = lite.connect("/var/GestionSysteme/service.db")
line_chart = pygal.Line()
with con:
	cur = con.cursor()
	data = cur.execute("Select date,information,machine from "+sys.argv[1]+" group by date having count(*)=(select count(distinct machine) from "+sys.argv[1]+" ) order by date")
	date = []
	user = {}
	for row in data:
		date.append(row[0])
		if not user.has_key(row[2]):
			user[row[2]] = []
		user[row[2]].append(float(row[1]))
	cur.close()

line_chart.title = 'Historique '+sys.argv[1]
line_chart.x_labels = date
for key in user.iterkeys():
	line_chart.add(key,user[key])
#line_chart.add(str(row[2]),row[1] )
line_chart.render_in_browser()



