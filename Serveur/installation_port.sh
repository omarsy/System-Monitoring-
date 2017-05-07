#!/bin/bash
#statements
##
##Permettant d'enregistrer une nouvelle machine et de lui attribuer un port
##
echo "Entrez le nom de la machine :"
read nom
echo "Entrez le port pour l'ecoute :"
read port 
insert_in_db.py /var/GestionSysteme/service.db port_machine port $port machine $nom
