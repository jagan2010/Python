#!/usr/local/bin/python3.7

import os
import json
import glob
import shutil

try:
    os.mkdir("./provisioned")
except OSError:
    print("Directory already exists")


subtotal = float(0.0)
files=glob.glob("./new/file-[0-9]*.json")

for i in files:
    with open(i,"r") as f:
        content=json.load(f)
        subtotal+=float(content["value"])
        name=i.split("/")[-1]
        shutil.move(i,f"./provisioned/{name}")

print("Subtotal: %.2f"%subtotal) 
