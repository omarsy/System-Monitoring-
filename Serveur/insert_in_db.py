#!/usr/bin/python
# -*- coding: utf-8 -*-
##
##Programme permettant l'insertion des donnees
##
##exemple : insert_in_db.py db_name nomtable colonne1 donnee1 colonne2 donnee2 ...
##

import sqlite3 as lite
import sys,os
DEFAULT_TAILLE="1"
FICHIER_CONFIG="config_Limite_Stockage"
FICHIER_Delete_data="delete_table_in_db.py"
#On recupere le configurations
taille_max=os.popen('cat '+FICHIER_CONFIG+' || echo '+DEFAULT_TAILLE)
taille_max = float(taille_max.read())
taille_act=os.popen("ls -la "+sys.argv[1]+"|cut -d' ' -f5")
taille_act = float(taille_act.read())/1000000
print sys.argv
if taille_max > taille_act :# SI la taille n'est pas superieur a la limite on continu de mettre le donnees
	db_name = sys.argv[1]
	table_name = sys.argv[2]

	script = "INSERT INTO " + table_name + " ("
	script2 = ") VALUES ("

	i = 3
	while i < len(sys.argv):
		if i != 3:
			script += ", "
			script2 += ", "
		script += sys.argv[i]
		script2 += "'" + sys.argv[i + 1] + "'"
		i = i + 2

	script = script + script2 + ")"

	con = lite.connect(db_name)

	with con:
		cur = con.cursor()
		v=cur.execute(script)
		cur.close()
else :
	os.popen(''+FICHIER_Delete_data+" "+db_name+" ram cpu NmbUserConnecte disque NmbProcessus ram temperature cert")
