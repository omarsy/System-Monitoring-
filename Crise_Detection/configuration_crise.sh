#!/bin/bash
##
##Choix du niveau maximum que peut atteindre les ressources
##

EMPLACEMENT_CONFIG="/etc/GestionSysteme/"
echo "processus : "
read process
echo "ram :"
read ram1
echo "disque :"
read disk
echo "temperature :"
read tmp
echo -e "process : $process\nram : $ram1\ndisque : $disk\ntemperature : $tmp">$EMPLACEMENT_CONFIG"configcrise"
