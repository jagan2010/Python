#!/usr/local/bin/python3.7

import subprocess
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("port",help="Enter port number")

args=parser.parse_args()
command=subprocess.run(["lsof","-n",f"-i4TCP:{args.port}"],stdout=subprocess.PIPE)
print(command.stdout.decode())
