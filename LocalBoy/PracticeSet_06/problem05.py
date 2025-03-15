# problem 05
# 5. Write a program which a finds whether given number is present in list or not.

number_list = [88, 45, 33, 67, 89, 4, 23, 78, 99, 0, 100]
user_defined_num = int(input("enter num: "))

if user_defined_num in number_list:
    print(f"{user_defined_num} number in a list")
else:
    print(f"{user_defined_num} not in list.")
