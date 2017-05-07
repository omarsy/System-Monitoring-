#!/bin/bash
##
##Recuperation de la temperature de la machine
##

temp=`sensors | grep 'temp1' |cut -d: -f2 |cut -d+ -f2 | cut -d. -f1`

echo "temperature date `date '+%m/%d/%y-%H:%M'` machine $HOSTNAME information $temp"
