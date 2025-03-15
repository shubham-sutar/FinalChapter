# problem 04
# 4. Write a program to find whether given user name contains less than 10 characters or not.

username = input("Enter your user name: ")
updated_user = len(username)

if updated_user >= 10:
    print(f"{updated_user} This username contains 10 or more characters.")
else:
    print(f"{updated_user} This username contains less than 10 characters")

