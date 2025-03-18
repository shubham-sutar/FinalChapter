# problem 05
# 5. Write a python function to print n times of the following pattern:
# n = 3

"""
***  3-1
**   3-2
*    3-3
"""


def star_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)


n = int(input("Enter any number: "))
star_pattern(n)
