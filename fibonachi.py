#!/usr/local/bin/python3.7
numb=int(input("Enter the maximum number: "))
fib_list=[0]
i = 0
j = 1
while i < numb:
    k = i + j
    if k >= numb:
        break
    fib_list.append(k)
    j = fib_list[-2]
    i = fib_list[-1]

print(fib_list[1:])
