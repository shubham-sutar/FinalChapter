# problem 02

# 2. Write a program to input eight numbers from the user and display all the unique numbers(once)

import time

num_list = []
my_num = int(input("enter 1st num: "))
num_list.append(my_num)
my_num = int(input("enter 2nd num: "))
num_list.append(my_num)
my_num = int(input("enter 3rd num: "))
num_list.append(my_num)
my_num = int(input("enter 4th num: "))
num_list.append(my_num)
my_num = int(input("enter 5th num: "))
num_list.append(my_num)
my_num = int(input("enter 6th num: "))
num_list.append(my_num)
my_num = int(input("enter 7th num: "))
num_list.append(my_num)
my_num = int(input("enter 8th num: "))
num_list.append(my_num)

time.sleep(2)
print(f"all entered numbers: {num_list}")
num_set = set(num_list)
time.sleep(2)
print(f"unique numbers is : {num_set}")




