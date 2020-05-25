#!/usr/local/bin/python3.7

import math

def ftruncate_num(num,j=0):
    if num and (j > 0):
        multi = (10 ** j)
        value = math.floor(num * multi)/multi
        return value
    else:
        return math.floor(num)

num = float(input("Enter the floating number: "))
digits = int(input("Enter the number of digits you want after dot: "))
output=ftruncate_num(num,digits)
print(output)
