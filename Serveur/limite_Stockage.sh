#!/bin/bash

##
##Programme permmettant de configurer la limite de stockage
##
##

EMPLACEMENT_CONFIG="/etc/GestionSysteme/"
echo "ENtrez la limite de taille (MO) :"
read taille

echo "$taille">$EMPLACEMENT_CONFIG"config_Limite_Stockage"
