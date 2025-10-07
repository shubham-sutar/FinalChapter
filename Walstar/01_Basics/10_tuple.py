# Tuple

numbers = ()  # empty tuple
print(type(numbers))

numbers = (12, 21, 34, 66, 78, 89, 12)
new_count = numbers.count(12)
print(new_count)

ind = numbers.index(66)
print(ind)

print(0 in numbers)  # False
print(89 in numbers)  # True



