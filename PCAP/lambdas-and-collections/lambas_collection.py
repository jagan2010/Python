#!/usr/local/bin/python3.7

people=[{"name":"jagadish","age":31,"gen":"Male"},{"name":"Vijay","age":29,"gen":"Male"},{"name":"Vicky","age":28,"gen":"Male"},{"name":"Bhagya","age":24,"gen":"Female"}]

print("List of people are: \n", people)

sorted_by_people = sorted(people,key=lambda dtn_var: dtn_var["name"].lower())
print("sorted people are :\n", sorted_by_people)

name_declaration=map(lambda d:  f"{d['name']} is now {d['age']} years old and gender={d['gen']}",sorted_by_people)
print("Name declaration is: \n")
print(list(name_declaration))
