# Tuples

chars = ('a', 'c', 'y', 'z', 'b')
print(type(chars))

# Empty Tuple
chars = ()
print(chars)

# Tuple with single element
chars = ('a')  # type str
char = ('a',)  # type tuple

print(type(chars))  # type str
print(type(char))  # type tuple

# Tuple methods
my_tuple = (12, 11, 23, 43, 56, 12, 11, 12, 12)

# count
redency = my_tuple.count(12)
print(redency)  # 12 occurs 4 times

# index
index_of_item = my_tuple.index(43)
print(index_of_item)  # 43 at 3 index

# index_of_item = my_tuple.index(99)
# print(index_of_item)  # error not in tuple


