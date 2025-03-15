# problem 02
# 2. write a program to find out whether is student passed or fail if it requires total number of 40% and atleast 33
# percent in subject to pass.

marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 2: "))
marks3 = int(input("enter marks 3: "))

# percentage
total_percentage = (marks1 + marks2 + marks3) * 100 / 300

# print("percentage: ", total_percentage)
if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print(f"your Passed {total_percentage} !!")
else:
    print(f"your Failed..{total_percentage} !!")
