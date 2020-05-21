#!/usr/local/bin/python3.7

class employee:
    

    def __init__(self,name):
        self.file_name=name


    def get_all(self):
        with open(self.file_name,"r") as f:
            for line in f.readlines():
                print(line.strip("\n"))


    def get_at_line(self,line_num=1):
        with open(self.file_name,"r") as f:
            return f.readlines()[line_num-1]
