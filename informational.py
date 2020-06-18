#!/usr/local/bin/python3.7

import subprocess
import sys
try:
    with open('/etc/oratab','r') as O:
        for line in O.readlines():
            if (line.find('dbhome') != -1):
                O_HOME=line.strip('\n').split(':')[1]
                O_BASE="/u01/app/oracle"
            elif (line.find('grid') != -1):
                G_HOME=line.strip('\n').split(':')[1]
                G_BASE="/u01/app/grid"
except FileNotFoundError as err:
    print("This is not a Db server, Since there is no oratab file.....Exiting")
    sys.exit(1)
command1=f"{G_HOME}/bin/crsctl stat res -w \"TYPE = ora.database.type\" -p |grep -E \"DB_UNIQUE_NAME|USR_ORA_DB_NAME|GEN_USR_ORA_INST_NAME@SERVERNAME\(`hostname`\)\""
pcommand1=subprocess.run([f"{command1}"],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,shell=True)
out=pcommand1.stdout.strip().split('\n')
for i in out:
    if i.startswith('DB_UNIQUE'):
        DB_UNIQUE_NAME=i.split('=')[1]
    elif i.startswith('GEN_USR_ORA'):
        INSTANCE_NAME=i.split('=')[1]
    elif i.startswith('USR_ORA'):
        DB_NAME=i.split('=')[1]


print("          INFROMATIONAL ONLY           ")
dash='-' * 80
print(dash)
print(f" DB_UNIQUE_NAME={DB_UNIQUE_NAME}\n INSTANCE_NAME={INSTANCE_NAME}\n DB_NAME={DB_NAME}")
print(dash)
print("===Important Filesystem usage on the server==")
for i in p1.stdout.split('\n')[1:]:
    j=i.split()[:-3:-1]
    if ("/u01" in j) or ("/" in j):
        print(f"{j[0]} file system is {j[1]} used")

