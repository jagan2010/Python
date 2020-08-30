#!/bin/python3
num=int(input("Enter a maximum number for fibonacci series:? "))
i=0
j=1
print("The series are:")
print(i+j,end=",")
while (j <= num):
    z=i + j
    if ( z > num):
        break 
    i=j
    j=z
    print(j,end=",")
print("")
