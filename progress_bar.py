#!/usr/bin/python3
import subprocess
from time import sleep
p1=subprocess.Popen(["sleep 20"],shell=True,stdout=subprocess.PIPE)
print('Task in progress',end='')
while ( p1.poll() == None ):
    print('.',end='',flush=True)
    sleep(1)
print()
