#!/usr/local/bin/python3.7

import time

def timer():
    now = time.localtime()
#    return f"Current Time : {now.tm_mday}-{now.tm_mon}-{now.tm_year} {now.tm_hour}:{now.tm_min}:{now.tm_sec}"
    return f"Current Time : {time.strftime('%X',now)}" 

while True:
    print(timer())
    time.sleep(1)
