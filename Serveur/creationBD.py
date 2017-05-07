#!/usr/bin/python
##
##Script nous permettant de creer la base de donnee
##
import sqlite3
conn = sqlite3.connect("/var/GestionSysteme/service.db")
C = conn.cursor();
C.execute('Create TABLE cpu (date text,machine text,information text)')
C.execute('Create TABLE NmbUserConnecte (date text ,machine text,information text)')
C.execute('Create TABLE disque (date text ,machine text,information text)')
C.execute('Create TABLE NmbProcessus (date text,machine text,information text)')
C.execute('Create TABLE ram (date text,machine text,information text)')
C.execute('Create TABLE temperature (date text,machine text,information text)')
C.execute('Create TABLE port_machine (port text,machine text)')
C.execute('Create TABLE cert (title text primary key,resume text,lien text)')
C.close()
