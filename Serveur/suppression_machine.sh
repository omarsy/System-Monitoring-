#!/bin/bash
#statements

##
##Programme permmetant de supprimer des machines
##
##
echo "Entrez le nom de la machine :"
read nom
echo "Entrez le port pour l'ecoute :"
read port


delete_in_db.py /var/GestionSysteme/service.db port_machine port $port machine $nom

