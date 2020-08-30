#!/bin/python3
num=int(input("Enter a number:? "))
i=0
j=1
while (j <= num):
    z=i + j
    if ( z > num):
        print(num,"is not a fibonacci number")
        break 
    elif (z == num):
        print(num,"is a fibonacci number")
        break
    i=j
    j=z
