#!/bin/bash
##
##Recuperation du nombre d'utilisateur qui est en entrain de s'executer
##
nmb=`who|wc -l`

echo "NmbUserConnecte date `date '+%m/%d/%y-%H:%M'` machine $HOSTNAME information $nmb"
