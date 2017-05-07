#!/usr/bin/python
import sqlite3 as lite
import feedparser,os,sendmail
DEFAULT_TAILLE="1"
FICHIER_CONFIG="/etc/GestionSysteme/config_Limite_Stockage"
FICHIER_SERVEUR="/var/GestionSysteme/service.db"
FICHIER_Delete_data="delete_table_in_db.py"
# chargement de la configuration
taille_max=os.popen('cat '+FICHIER_CONFIG+' || echo '+DEFAULT_TAILLE)
taille_max = float(taille_max.read())
taille_act=os.popen("ls -la "+FICHIER_SERVEUR+"|cut -d' ' -f5")
taille_act = float(taille_act.read())/1000000

if taille_max <= taille_act :# SI la taille est  superieur a la limite on supprime les donnees
	os.popen('./'+FICHIER_Delete_data+" "+FICHIER_SERVEUR+" ram cpu NmbUserConnecte disque NmbProcessus ram cert")
#Recherche d'alerte 
d = feedparser.parse('http://www.cert.ssi.gouv.fr/site/cert-fr.rss ')
v=d.entries
con = lite.connect(FICHIER_SERVEUR)
with con:
	for ent in d.entries :
		titre = ent.title.encode('utf-8')		
		lien=ent.link.encode('utf-8')
		description=ent.description.encode('utf-8')
		script = "INSERT INTO  cert (title ,resume ,lien) values ('"+str(titre)+"','"+str(description)+"','"+str(lien)+"')"
		cur = con.cursor()		
		try :
			cur.execute(script)# Enregistrement dans la base	
			mess = os.popen("mail_cert.sh "+titre+ " "+description+" "+" "+lien)
			mess = mess.read() 			
			sendmail.mail('cert',mess)
		except :
			print ""		
		cur.close()
print mess
#u'For documentation <em>only</em>'

