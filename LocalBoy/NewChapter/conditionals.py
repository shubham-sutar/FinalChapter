# Conditionals
"""
age = int(input("enter your age: "))

if age > 18:
    print("your Eligible for vote.")
elif age < 0:
    print("Wrong age entered")
else:
    print("enter your not eligible for vote.")

print("Program End")

age = input("your age is greater than 18 type yes or no: ")

if age == "yes":
    print("your eligible for vote")
else:
    print("your not eligible")

print("Program End")

msg1 = "make a lot of money"
msg2 = "buy now"
msg3 = "subscribe this"
msg4 = "click this"

message = input("enter your comment here: ")
if (msg1 in message) or (msg2 in message) or (msg3 in message) or (msg4 in message):
    print("Spam msg detected")
else:
    print("msg not under spam")
"""

username = input("Enter the username: ")

if (len(username)) < 10:
    print("username requires more than 10 letters")
else:
    print("All is well")
