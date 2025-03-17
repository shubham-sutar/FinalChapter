# problem 05
# 5. Write a program to find the sum of first 10 numbers of natural number by using while loop.


num = int(input("Enter any num: "))
i = 1
sum = 0
while i <= num:
    sum = sum + i
    i = i + 1

print(f"sum of 10 numbers: {sum}")

