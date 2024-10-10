# Filters in python
# The filter function in python is a built-in function
# allows you to filter elements in the list, tuple, set

"""
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

for k, v in my_dict.items():
    if k == 'b':
        print("Key with name b found")

op = 'b' in my_dict
print(op)
"""

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# even_num = []
#
# for i in numbers:
#     if i % 2 == 0:
#         temp = i
#         even_num.append(temp)
#
# print(even_num)

# Use Filter()
"""
def even_num(num):
    return num % 2 == 0


even_num_list = list(filter(even_num, numbers))
print(even_num_list)
"""

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda num: num % 2 == 0

even_list = list(filter(even, numbers))
print(even_list)
"""


# Recursion
# Recursion is a programming technique where a function
# call itself in order to solve a problem

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))
