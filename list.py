#!/usr/local/bin/python3.7
users=[]
users.append("Jagadish")
users.append("Bhagya")
users.append("Rudra")
users.append("buddy")
print(users)
del users[3]
rev_users= list(reversed(users))
print(rev_users)
users.insert(3,"Buddy")
users+=["vijay","vikram","mahalakshmi"]
print(users)
print(users[2:4])
