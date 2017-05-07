#!/bin/bash

##
##Script permettant de recuperer le mail par defaut et de remplace les valeurs ou ##envoie l'etat seulement
##
##
information=$1
FICHIER_MAIL="/tmp/GestionSysteme/mail_alerte"
mess=`cat $FICHIER_MAIL` || mess="Etat $1"
echo `echo $mess | sed  "s/value_info/$information/"`
