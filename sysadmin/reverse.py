#!/usr/local/bin/python3.7

import sys
import argparse

parser=argparse.ArgumentParser("Description: searching a word")
parser.add_argument("filename",help="filename is must")
parser.add_argument("--limit","-l",type=int,help="Number of lines")

args = parser.parse_args()

with open(args.filename,"r") as f:
    lines=f.readlines()
    rev_str=[]
    for line in lines[0:args.limit]:
        word=line[::-1].strip() 
        rev_str+=[word] 

print(list(reversed(rev_str)))
