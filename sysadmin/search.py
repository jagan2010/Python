#!/usr/local/bin/python3.7

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="keyword is must to search")

args=parser.parse_args()
#print(args)
with open("names.txt","r+") as f:
    words=f.readlines()

print([word.strip() for word in words if args.keyword in word.lower()])
