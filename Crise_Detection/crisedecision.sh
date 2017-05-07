#!/bin/bash
##
##Fonction nous permettant de choisir les crises qui sont importants
##
##

##Fonction permmettant de controler qu'on taper la bonne valeur c'est dire "o" ou "n"
lecture ()
{
EMPLACEMENT_CONFIG="/etc/GestionSysteme/"
v=1
echo $*
type=`echo $*|cut -d ' ' -f8`
while [ $v -eq 1 ]
do
echo "oui appuyer[o] ou non appuyer[n]" 
read val

if [ $val = "o" ]
then
text="$text\n$type : 1"
v=0
elif [ $val = "n" ]
then
text="$text\n$type : 0"
v=0
fi
done
}
export text
lecture "Voulez vous etre averti a cause du ram :"

lecture "Voulez vous etre averti a cause du temperature :"
lecture "Voulez vous etre averti a cause du disque :"

lecture "Voulez vous etre averti a cause du processeur :"

echo -e $text >$EMPLACEMENT_CONFIG configdecision
