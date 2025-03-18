# problem 08
# 8. Write a python function to print multiplication table of a given number


def mult_table(num):
    for i in range(1, 11):
        print(f"{i} x {num} = {i * num}")


num = int(input("Enter num: "))
mult_table(num)
