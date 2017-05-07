#!/usr/bin/python
import sqlite3 as lite
import sys,os
import pygal
##
#
#Script nous permettant de mettre en place l'interface web
#
#

#Connection a la base de donnees
con = lite.connect("/var/GestionSysteme/service.db")

content ="<!DOCTYPE HTML>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n<style type=\"text/css\"> \n [class*=\"col\"] { margin-bottom: 20px; }\nimg { width: 100%; }\n body { margin-top: 10px; }\n </style>\n</head>\n <body>"

##
##Recuperation des donnees  des serveur et mettre en place l'interface web approprie
##

entete = "<thead>\n<tr>\n<th>RAM</th>\n<th>CPU</th>\n<th>DISQUE</th>\n<th>Nombre de Processus</th>\n<th>Temperature</th> \n<th>Nombre d'Utlisateur</th></tr></thead>"
with con:
	cur = con.cursor()
	data = cur.execute("Select distinct machine from port_machine");
	for machine in data :
		cur1 = con.cursor();
		content += "<table class=\"table table-inverse\">\n<h1 postion>Serveur : "+machine[0]+"</h1>"
		content +=entete+"\n<tbody>\n"
		donne = cur1.execute("Select ram.information,cpu.information ,disque.information,NmbProcessus.information,temperature.information,NmbUserConnecte.information from ram,cpu,NmbUserConnecte,disque,NmbProcessus,temperature where ram.machine='"+machine[0] +"' and cpu.machine='"+machine[0]+"' and disque.machine='"+machine[0]+"' and NmbProcessus.machine='"+machine[0]+"' and temperature.machine='"+machine[0]+"' and NmbUserConnecte.machine='"+machine[0]+"' Order by ram.date Limit 5")
		try :
			for row in donne : 
				content +="<tr>\n"
				for value in row :
					content +="<td>"+value+"</td>\n"
				content +="</tr>\n"
		except :
			content +="<td>-<td>\n<td>-<td>\n<td>-<td>\n<td>-<td>\n<td>-<td><td>-<td>"
		content += "</tbody>\n</table>\n"
		cur1.close()

	cur.close()
	cur = con.cursor()

###
###Recuperation des donnees  de cert et mis en place de l'interface web approprie
###

	data = cur.execute("Select * from cert LIMIT 5");
	content += "<table class=\"table table-inverse\">\n<h1>CERT :</h1>"
	content +="<thead>\n<tr>\n<th>TITRE</th>\n<th>RESUME</th>\n<th>LIEN</th></tr></thead>\n<tbody>\n"
	for row in data : 
				content +="<tr>\n"
				i=0
				for value in row :
					if i != 2 :
						content +="<td>"+value+"</td>\n"
					else :
						content +="<td> <a href='"+value+"'> Visiter </a></td>\n"
					i=i+1
				content +="</tr>\n"
content += "</body>\n</html>"
print content
os.popen("echo  \""+content.encode('utf-8') +"\" >/etc/GestionSysteme/InterfaceWeb/a.html")

os.popen("firefox /etc/GestionSysteme/InterfaceWeb/a.html")
