#!/usr/local/bin/python3.7

import subprocess
import json
import shutil
import glob

receipts=glob.glob("./new/file*")
subtotal=0

for file in receipts:
    with open(file,"r") as f:
        content=json.load(f)
        subtotal+=float(content["value"])
        name=file.split("/")[-1]
    shutil.move(f"{file}",f"./provisioned/{name}")
    print("file moved from",file,"to ./provisioned/"+name)

print("Total Sum is :", subtotal)
