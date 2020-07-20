#!/usr/local/bin/python3.7

class classy:
    counter=1
    def __init__(self):
        self.a=1
        self.b=2
        self.c=__name__
    def sum(self):
        classy.counter+=1
        return self.a + self.b
     
    def result(self):
        self.sum()

    print(__name__)
