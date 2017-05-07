#!/usr/bin/python
 # -*- coding:Utf-8 -*-

##
##Programme qui cherche est ce que les ressources n'ont pas atteint la limite fixe
## si c'est le cas on l'envoie par mail a l'administrateur
##
##
##

import os
import re,psutil
import sendmail
os.popen('clear')
ADRESS_CONFIG = "/etc/GestionSysteme/" #Adresse ou se trouve les fichiers de configuration dans la machine

DEFAULT_VALUE="70" # Valeur par defaut
DEFAULT_DECISION="1" # la decision par defaut

#Recuperation des decisions dans configdecision
cpu_crise_decision = os.popen("(cat"+ADRESS_CONFIG +"configdecision|| echo processus:"+DEFAULT_DECISION+") | grep -E '^process' | cut -d':' -f2 ")
cpu_crise_decision = int(cpu_crise_decision.read())
ram_crise_decision = os.popen("(cat"+ADRESS_CONFIG +"configdecision|| echo ram: "+DEFAULT_DECISION+") | grep -E '^ram' | cut -d':' -f2")
ram_crise_decision = int(ram_crise_decision.read())
disk_crise_decision = os.popen("(cat"+ADRESS_CONFIG +"configdecision|| echo disque: "+DEFAULT_DECISION+") | grep -E '^disque' | cut -d':' -f2")
disk_crise_decision = int(disk_crise_decision.read())
cpu_temp_crise_decision = os.popen("(cat"+ADRESS_CONFIG +"configdecision|| echo temperature:"+DEFAULT_DECISION+") | grep -E '^temperature' | cut -d':' -f2 ")
cpu_temp_crise_decision = int(cpu_temp_crise_decision.read())


#Recuperation des donnees crise dans le fichie configcrise
cpu_crise = os.popen("(cat"+ADRESS_CONFIG +"configcrise || echo process:"+DEFAULT_VALUE+ ")| grep -E '^process' | cut -d':' -f2")
cpu_crise = int(cpu_crise.read())
ram_crise = os.popen("(cat"+ADRESS_CONFIG +"conficrise || echo ram:"+DEFAULT_VALUE+ ")| grep -E '^ram' | cut -d':' -f2")
ram_crise = int(ram_crise.read())
disk_crise = os.popen("(cat"+ADRESS_CONFIG +"conficrise || echo disque:"+DEFAULT_VALUE+ ")| grep -E '^disque' | cut -d':' -f2")
disk_crise = int(disk_crise.read())
cpu_temp_crise = os.popen("(cat"+ADRESS_CONFIG +"conficrise || echo temperature:"+DEFAULT_VALUE+ ") | grep -E '^temperature' | cut -d':' -f2")
cpu_temp_crise = int(cpu_temp_crise.read())

# Recuperation de l'etat actuel des ressources
buff=os.popen('sensors')
infos=buff.read().replace('+', '').replace(' ', '')
buff.close()
cpu_temp = re.findall('temp1:([0-9]*)', infos)[0]
cpu_temp = float(cpu_temp)
pmem = float(psutil.virtual_memory()[2])
cpu = float(psutil.cpu_percent(interval=1))
disk = float(psutil.disk_usage('/')[3])


#Verifier est ce que c'est en sitution de crise
text = "\n"
if cpu_crise_decision and cpu >= cpu_crise :
	buff = os.popen("mail_alerte.sh "+str(cpu))
	text = buff.read()
	buff.close()
	sendmail.mail("Niveau Critique CPU ",str(text))
if ram_crise_decision and pmem >= ram_crise :
	buff = os.popen("mail_alerte.sh "+str(pmem))
	text = buff.read()
	buff.close()
	sendmail.mail("Niveau Critique RAM",str(text))
if disk_crise_decision and disk >= disk_crise:
	buff = os.popen("mail_alerte.sh "+str(disk))
	text = buff.read()
	buff.close()
	sendmail.mail("Niveau Critique Disque",str(text))
if cpu_temp_crise_decision and cpu_temp >= cpu_temp_crise :
	buff = os.popen("mail_alerte.sh "+str(cpu_temp))
	text = buff.read()
	buff.close()
	sendmail.mail("Niveau Critique Temperature",str(text))



