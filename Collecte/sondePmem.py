#!/usr/bin/python
#
#Recuperation du pourcentage de memoire utilise
#
import psutil,os,time
pmem = psutil.virtual_memory()
pmem = os.popen("echo '" +str(pmem)+"' |cut -d',' -f3|cut -d'=' -f2")
#date = os.popen('date "+%m/%d/%yet%H:%M:%S"')
print 'ram date '+time.strftime("%m/%d/%y-%H:%M")+" machine "+os.uname()[1]+" information "+str(float(pmem.read()))


