#!/usr/bin/python
# -*- coding: utf-8 -*-
##
##Permettant de supprimer les donnees 
##
##Les critere sont passee en argument 
## 
##exemple : delete_in_db.py nomdelabase nomdelatable colonne1 critere1 colonne2 critere2...
##
import sqlite3 as lite
import sys

db_name = sys.argv[1]
table_name = sys.argv[2]

script = "DELETE FROM " + table_name + " WHERE "

i = 3
while i < len(sys.argv):
	if i != 3:
		script += " AND "
	script += sys.argv[i] + " = '" + sys.argv[i + 1] + "'"
	i = i + 2

con = lite.connect(db_name)

with con:
	cur = con.cursor()
	cur.execute(script)
	cur.close()

print script
