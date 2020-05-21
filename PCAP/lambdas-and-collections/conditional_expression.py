#!/usr/local/bin/python3.7

name=input("Enter your name: ?")

print("your name is longer than 10 characters") if len(name)>=10 else print("your name is less than 10 characters")

for letter in name:
#    print(f"{letter} {'is a vowel' if letter.lower() in ['a','e','i','o','u'] else 'is a constant'}")
     print(letter,"is a vowel" if letter.lower() in ['a','e','i','o','u'] else "is a constant")
