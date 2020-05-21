#!/usr/local/bin/python3.7

def split_func(name):
    first_name=name.split()[0]
    last_name=name.split()[-1]
    return (first_name,last_name)

def is_palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False

Ename=input("Enter your name(ex:Firstname lastname)? ")
result=split_func(Ename)
print("{} is my first name,{} is my last name".format(result[0],result[1]))

Pname=input("Enter any name(check for palindrome) ? ")
if is_palindrome(Pname):
    print("{} is a palindrome".format(Pname))
else:
    print("{} is a not palindrome".format(Pname))
