#!/usr/local/bin/python3.7
colors=["blue","white","green","yellow","red","purple","orange"]
liked_colors=[col for col in colors if col not in ["red","orange"]]
print(liked_colors)
