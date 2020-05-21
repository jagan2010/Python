#!/usr/local/bin/python3.7
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

item_to_calculate = int(input("what item to calculate? "))
print(fib(item_to_calculate))
