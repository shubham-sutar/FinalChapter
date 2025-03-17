# problem 03
# 3. write a program to print multiplication table of given number using while loop.

num = int(input("Enter any Number: "))
i = 1
while i < 11:
    result = i * num
    print(f"{i} x {num} = {result}")
    i = i + 1

