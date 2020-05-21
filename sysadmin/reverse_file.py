#!/usr/local/bin/python3.7

import argparse
import sys

parser = argparse.ArgumentParser("Description: To reverse a file")
parser.add_argument("filename", help="Filename is must")
parser.add_argument("--limit" , "-l" , type=int ,help="Limit number of lines")
parser.add_argument("--version", "-v", action="version" , version="%(prog)s version 1.0")

args=parser.parse_args()

try:
    with open(args.filename,"r+") as f:
        limit=args.limit
except FileNotFoundError as err:
    print(f"\nError : {err}") 
    sys.exit(1)
else:
    with open(args.filename,"r+") as f:
        lines=f.readlines()

        if limit:
            lines.reverse()
            for i in lines[:limit]:
                print(i.strip()[::-1]) 
