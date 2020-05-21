import sys
import random

try:
    print(F"received with thanks from :{sys.argv[1]}")
    args=sys.argv
    print(args)
    random.shuffle(args)
    print(args)
except(IndexError) as err:
    print(f"Error: No arguments , Please provide at least one {err}")
    
