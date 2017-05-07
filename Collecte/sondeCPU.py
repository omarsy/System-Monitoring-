#!/usr/bin/python
##
## Recuperation des donnees des processeurs
##
import psutil,time,os
v = psutil.cpu_percent(interval=1)
print 'cpu date '+time.strftime("%m/%d/%y-%H:%M")+" machine "+os.uname()[1]+" information "+str(v)

