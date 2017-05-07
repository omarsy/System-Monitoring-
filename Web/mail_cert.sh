#!/bin/bash
titre=$1
resume=$2
lien=$3
FICHIER_MAIL="/tmp/GestionSysteme/mail_cert"
mess=`cat $FICHIER_MAIL`|| mess="titre : $1 resume : $2 lien: $3"
echo `echo $mess |  sed  "s/value_titre/$titre/" |sed "s/value_resume/$resume/"|sed "s/value_lien/$lien/"` 

