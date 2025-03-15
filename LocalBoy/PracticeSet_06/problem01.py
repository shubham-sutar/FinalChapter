# problem 01
# 1. write a program to find the greatest of four numbers entered by user
"""
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))
fourth_num = int(input("Enter fourth number: "))

if first_num > second_num and first_num > third_num and first_num > fourth_num:
    print(f"First number {first_num} is greatest.")
elif second_num > third_num and second_num > first_num and second_num > fourth_num:
    print(f"Second number {second_num} is greatest.")
elif third_num > first_num and third_num > second_num and third_num > fourth_num:
    print(f"Third number {third_num} is greatest")
elif fourth_num > first_num and fourth_num > second_num and fourth_num > third_num:
    print(f"Fourth number {fourth_num} is greatest")
else:
    print("invalid operation")
"""

my_list = []
my_num = int(input("Enter any first number: "))
my_list.append(my_num)
my_num = int(input("Enter any second number: "))
my_list.append(my_num)
my_num = int(input("Enter any third number: "))
my_list.append(my_num)
my_num = int(input("Enter any fourth number: "))
my_list.append(my_num)

print(f"The greatest number is : ", max(my_list))


