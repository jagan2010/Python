#!/usr/local/bin/python3.7

import time
#from time import localtime,mktime,strftime

start_time=time.localtime()
print(f"starting time is :{time.strftime('%X',start_time)}")
input("press 'Enter' to stop")
stop_time=time.localtime()
print(f"starting time is :{time.strftime('%X',stop_time)}")
difference=time.mktime(stop_time) - time.mktime(start_time)
print("Difference is :",difference)
