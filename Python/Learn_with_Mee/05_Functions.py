# Break and Continue


# Break
"""
for i in range(1, 11):
    print(i)
    if i == 5:
        break
print("program Stopped")
"""

# Continue
"""
for i in range(1, 11):
    if i == 5:
        continue
    else: 
        print(i)
print("program Stopped")

for i in range(10):
    if i == 5:
        pass
    else:
        print(i)
"""

# Reversed()
"""
for i in reversed(range(0, 10)):
    print(i)
"""

# Switch (Match) Case
"""
num = int(input("Enter your Luck num 1 to 3:"))

match num:
    case 3:
        print("you good person with good heart")
    case 2:
        print("Your Healthy")
    case 1:
        print("You are superman")
    case _:
        print("Invalid selection")
"""


# Functions
# Python is all about the functions
# A- Chat
# built - in
# print, max, min, len, id, upper, reversed

# user defined functions
# syntax to create own function
# defined
# calling it

# def greet():
#     print("Hello, How are you")
#
#
# greet()

# pass some info to the f(n)
def test_name(name):
    print(f"Hello how are you {name}")


test_name("shubham")


def pass_find(name, password):
    if name == "shubham":
        if password == "123":
            print("welcome Bhai")
        else:
            print("nikal be")


pass_find("shubham", "123")

