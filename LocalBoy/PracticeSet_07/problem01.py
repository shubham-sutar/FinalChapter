# problem 01

# 1. write a program to print multiplication table of given number using for loop.

num = int(input("Enter any number: "))
for items in range(1, 11):
    result = num * items
    print(f"{items} x {num} = {result}")


