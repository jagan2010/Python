#!/usr/local/bin/python3.7
def build_item(item,count=1):
    list_item=[]
    for _ in range(count):
        list_item.append(item)
    return list_item


Eitem=input("Enter the item: ?")
htime=int(input("How many times: ?"))
print(build_item(Eitem,count=htime))

