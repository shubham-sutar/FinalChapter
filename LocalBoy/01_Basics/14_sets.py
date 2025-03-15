# Sets

my_set = {34, 56, 78, 90, "hello", 0, 0, 78}
print(my_set)

# Set Methods

# Add
my_set.add("sakura")
print(my_set)

# Operations on Set

print(len(my_set))
print(my_set.remove("hello"))
print(my_set)
clear = my_set.clear()
print(my_set)

# Union
my_set1 = {34, 56, 78, 90, "hello", 0, 0, 78}
my_set2 = {118, 200, 100, 199, "bye", 0, 78, 34}

new_set = my_set1.union(my_set2)
print(new_set, len(new_set), type(new_set))

# Intersection
new_set1 = my_set1.intersection(my_set2)
print(new_set1)
