#!/usr/bin/python
##
##Supprime une table passee en argument 
##exemple delete_table_in_db.py nomdb nomtable1 nomtable2 ...
#
import sqlite3 as lite
import sys

db_name = sys.argv[1]

script = "DELETE FROM " 
con = lite.connect(db_name)
i = 2
with con:
	while i < len(sys.argv):	
		cur = con.cursor()
		cur.execute(script+sys.argv[i])
		cur.close()
		i = i + 1
