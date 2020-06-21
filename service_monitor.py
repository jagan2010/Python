#!/usr/local/bin/python3.7
# Python script to monitor a service and logs it
# syslog for start/stop/check

import syslog
import re
import argparse
import sys
import subprocess
import time

def servicecheck():
    syslog.openlog(ident=args.service_name)
    a=subprocess.run([f"{command}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True,text=True)
    if re.search('.*active\s\(running\).*',a.stdout):
        syslog.syslog('Service Is running')
    else:
        syslog.syslog('Service NOT running')

parser=argparse.ArgumentParser('Description=Service monitor')
parser.add_argument('service_name',help='service name to monitor is mandatory')
args=parser.parse_args()
command=f"/bin/systemctl status {args.service_name}"

while True:
    servicecheck()
    time.sleep(10)
