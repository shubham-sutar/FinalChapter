# problem 07
# 7. write a program to print the following the pattern.
"""
for n = 3
  *
 ***
*****
"""

n = int(input("enter any number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")

