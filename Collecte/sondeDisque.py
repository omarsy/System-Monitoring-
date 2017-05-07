#!/usr/bin/python
##
##Recuperation du pourcentage de disque utilise
##

import os,re,time

disk = os.popen('df /')

disk = disk.read()
disk = re.findall('([0-9]*)%',disk)[1]
print 'disque date '+time.strftime("%m/%d/%y-%H:%M")+" machine "+os.uname()[1]+" information "+str(disk)

	
