# problem 09
# 9. write a program to print the following the pattern.
"""
for n = 3

***
* *
***

"""

n = int(input("Enter any num: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)  # Print full row of stars for first and last row
    else:
        print("*" + " " * (n - 2) + "*")  # Print star at start and end, spaces in between
