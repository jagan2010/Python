#!/usr/local/bin/python3.7
y = 5

def set_x(z):
    x=z
#    global y
    y=20
    print("y inside function is:",y)
    print("x inside function is:",x)
#    global y


set_x(10)
print("y outside function is:",y)
