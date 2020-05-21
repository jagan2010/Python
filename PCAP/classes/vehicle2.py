#!/usr/local/bin/python3.7

class vehicle2:

    def __init__(self,engine,tires=4):
        self.engine=engine
        self.tires=tires

    def description(self):
        return f"A {self.__class__.__name__} with {self.engine} and having {self.tires}"
