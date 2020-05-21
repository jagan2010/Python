#!/usr/local/bin/python3.7
count = 0
while count < 25:
    if ( count % 2) == 0:
        count+=1
        continue
    print("odd numbers are: ",count)
    count+=1
