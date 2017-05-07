#!/bin/bash
##
##Sonde qui recupere le nombre de processus qui est entrain de s'executer
##
	
v=`ps -aux |wc -l`

echo "NmbProcessus date `date '+%m/%d/%y-%H:%M'` machine $HOSTNAME information $v"	

