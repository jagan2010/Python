#!/usr/local/bin/python3.7
emails={"jagadish":"jagadish.uddandam@gmail.com","bhagya":"sreebhagi12@gmail.com","vijay":"vijay5b4@gmail.com"}
print(emails)
del emails["vijay"]
print("After deleting vijay email: \n",emails)
emails["vicky"]="vikramdev@gmail.com"
print("after addition vicky email: \n",emails)
users=list(emails.keys())
email_list=list(emails.values())
print("users:",users)
print("email_list:",email_list)
print(list(emails.items()))
