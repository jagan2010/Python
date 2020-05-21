#!/usr/local/bin/python3.7
name=input("what is yur name? ")
if len(name) >= 6:
    print("your name is long")
elif len(name) == 5:
    print("you name has 5 leetters only")
elif len(name) >= 4:
    print("you name is 4 or more characters")
else:
    print("your name is too short")
