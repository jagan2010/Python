#!/usr/local/bin/python3.7
value=input("enter a value: ")
if ((int(value) % 3 ) == 0) and ((int(value) % 5 ) == 0):
    print("Fizzbuzz")
elif ((int(value) % 3 ) == 0):
    print("fizz")
elif ((int(value) % 5 ) == 0):
    print("buzz")
else:
   print("booz")
