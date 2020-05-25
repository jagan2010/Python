#!/usr/local/bin/python3.7
# Author :- Jagadish.uddandam@oracle.com
# Python3 script for Oracle database RMAN Backup
# You must Give one argument passed to this script
# FULL - rmanBackup-FULL-template.rcv
# INCR - rmanBackup-INC-template.rcv
# ARCH - rmanBackup-ARC-template.rcv
# This applies to a single Database running ona server
# To support multiple databases , we need to add some function from line 40 through line 42

import subprocess
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Backup_filename",help="Full - rmanBackup-FULL-template.rcv, INCR - rmanBackup-INC-template.rcv, ARCH - rmanBackup-ARC-template.rcv")

args=parser.parse_args()

rmanscriptpath="/home/oracle/python_scripts"
rmanlogpath="/home/oracle/python_scripts"
scriptdate=time.strftime('%Y%m%d',time.localtime())



try:
    with open('/etc/oratab','r') as O:
        for line in O.readlines():
            if ( line.find('dbhome') != -1 ):
                O_HOME=line.strip().split(':')[1]
            elif ( line.find('grid') != -1 ):
                G_HOME=line.strip().split(':')[1]

except FileNotFoundError:
    print("There is no /etc/oratab on the server...exiting")
    sys.exit(1)

else:
    command=f"{G_HOME}/bin/crsctl stat res -w \"TYPE = ora.database.type\" -p |grep \"GEN_USR_ORA_INST_NAME@SERVERNAME(`hostname -s`)\""
    p1=subprocess.run([f"{command}"],stdout=subprocess.PIPE,shell=True,text=True)
    inst=p1.stdout.strip().split('=')[-1]
    rman_comand=f"{O_HOME}/bin/rman target / cmdfile={rmanscriptpath}/{args.Backup_filename} log={rmanlogpath}/rman_{inst}_{scriptdate}.log append"
    p3=subprocess.run([f"{rman_comand}"],stdout=subprocess.PIPE,shell=True,text=True,stderr=subprocess.DEVNULL)

    if (p3.returncode == 1):
        print("There is a problem with rman backup,Please check manually")
    else:
        print("RMAN Backup successfully completed")

