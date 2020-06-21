#!/usr/local/bin/python3.7
import math
number=float(input('Enter the floating number: '))
precision=int(input('Enter the floating number: '))

r = number * (10 ** precision)
a= math.floor(r) / (10 ** precision)
print(a)
