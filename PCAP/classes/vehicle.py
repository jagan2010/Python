#!/usr/local/bin/python3.7

class vehicle:

    def __init__(self,engine,tires=None):
        self.engine=engine
        self.tires=tires

    
#    def description(self):
#        print(f"A {__class__.__name__} is having {self.engine} and {self.tires} tires")

    def description(self):
        return f"A {self.__class__.__name__} is having {self.engine} and {self.tires} tires"
