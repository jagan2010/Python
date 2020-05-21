#!/usr/local/bin/python3.7

import subprocess
import argparse
import os

parser=argparse.ArgumentParser("Description: Checking status of service\n")
parser.add_argument("Service_name",help="Service name is mandatory")
args=parser.parse_args()

print(f"Checking status of the service({args.Service_name})")

p1=subprocess.run(["/bin/systemctl","status",f"{args.Service_name}"],stdout=subprocess.PIPE)


try:
    out=p1.stdout.decode().index("(running)")
except ValueError:
    print(f"{args.Service_name} service is down")
else:
    print(f"{args.Service_name} service is up")

