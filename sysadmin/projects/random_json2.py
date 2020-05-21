#!/usr/local/bin/python3.7

import os
import shutil
import random
import json


count=int(os.getenv("FILE_COUNT") or 100)
words=[word.split() for word in open("/usr/share/dict/words","r").readlines()]


for i in range(count):
    amount=random.uniform(1.0,1000)
    content={
        "topic":random.choice(words),
        "value":"%.2f"%amount
            }

    with open(f"./new/file-{i}.json","w") as f:
        json.dump(content,f)


