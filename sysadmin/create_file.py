#!/usr/local/bin/python3.7

import argparse as ag


parser = ag.ArgumentParser("\nDescription: To create a file")
parser.add_argument("Filename" , help="Filename to create")
parser.add_argument("--lines","-l",help="number of lines in the file")
args = parser.parse_args()
print(args)

with open(args.Filename,"w+") as f:
    f.writelines(["Bhagya\n",
                  "jagadish\n",
                  "Rudra\n",
                  "Vijay\n",
                  "Vicky\n"])

with open(args.Filename,"r+") as g:
    lin=g.readlines()

for i in lin:
    print(i.strip())  
