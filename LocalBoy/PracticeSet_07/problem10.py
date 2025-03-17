# problem 10
# 10. Write a program to display a revwers table of given number.

num = int(input("Enter any number: "))
for i in range(1, 11):
    table_num = f"{11 - i} X {num} = {(11 - i) * num}"
    print(table_num)
"""
logic :
1  10    11 - 1 = 10
2   9    11 - 2 = 9
3   8    11 - 3 = 8
4   7
5   6
6   5
7   4
8   3
9   2
10  1
"""