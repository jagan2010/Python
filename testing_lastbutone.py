#!/usr/local/bin/python3.7
numb=int(input("enter a number: "))
for i in range(1, numb+1):
    if (i % 3) == 0 and (i % 5) ==0:
        print("FizzBuzz")
    elif (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")

