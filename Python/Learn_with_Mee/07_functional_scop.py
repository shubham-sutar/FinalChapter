# Functional Scope
"""
def test_fun():
    a = 10
    local_var = 34
    print("hello world")
    print(a)


test_fun()
"""
"""
def test1():
    print("outer function")

    def test2():
        print("this is a inner function")


test1()
"""

"""
numbers = [12, 13, 14, 15]


def do_something(numbers_list):
    numbers_list.append(45)
    return numbers


my_numbers = do_something(numbers)
print(my_numbers)
"""
"""
cust_list = ["Naruto", "Shijuney", "hinata", "sakura"]


def my_clients(cust_list_):
    cust_list_.append("Sasuke")
    return cust_list_


company_clients = my_clients(cust_list)
print(company_clients)
"""

"""
num = [1, 2, 3, 4, 5, 6]


def my_nums(updated_num):
    updated_num.append(7)
    return updated_num


new_num_list = my_nums(num)
print(new_num_list)
"""

"""
num = [1, 2, 3, 4, 5, 6]


def my_nums(updated_num):
    updated_num.extend([67, 34, 66])
    return updated_num


new_num_list = my_nums(num)
print(new_num_list)
"""

# Lambda EXpression
"""
f_name = lambda name: name + " Sutar"
print(f_name("Sayali"))

f_double_payment = lambda salary: salary*2
print(f_double_payment(8000))
"""

"""
upper_fun = lambda name: str.upper(name)
print(upper_fun("sayali"))
"""

"""
# even odd
f_even_odd = lambda num: "even" if num % 2 == 0 else "odd"
print(f_even_odd(7))
"""

"""
def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


even_odd(55)
"""

"""
sort_this_list = [12, 11, 45, 78, 54, 67, 32, 567]
sort_this_list.sort()
print(sort_this_list)
"""

# square number
"""
pow_num = lambda num: num * num
print(pow_num(5))
"""
"""
my_list = [2, 3, 4, 5]
temp_list = []
for i in my_list:
    temp = i*2
    temp_list.append(temp)

print(temp_list)
"""

"""
my_list = [1, 2, 3, 4, 5]


# def double_item(num):
#     return num * 2

double_item = lambda num: num**2

double_list = list(map(double_item, my_list))
print(double_list)
"""

"""
my_list = [1, 2, 3, 4, 5]

double_list = list(map(lambda num: num ** 2, my_list))
print(double_list)

my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 23 # Immutable
print(my_tuple)
"""