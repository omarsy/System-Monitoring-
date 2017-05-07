#!/bin/bash
##
##Charger d'ecouter les ports passe en argument
##exemple : ouvrir_des_ports.sh port1 port2 ...
##

for param in $*
do
	#statements	
	nc -k -l $param | tache_exec.sh& 


sleep 1
done
wait
