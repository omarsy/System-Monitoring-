#!/bin/bash
##
## Script permettant s'inserer les donnees dans la base
## fonction a mettre a lier avec les donnes recues dans un port
##
while [[ true ]]
do
read var
var=`echo $var|grep 'date'` # necessiare pour repere les tubes vides
if [ "$var" != "" ] # si il n' a rien donc ce n est pas le bon jeu
then
insert_in_db.py /var/GestionSysteme/service.db $var # on execute la requete passee
fi
done
