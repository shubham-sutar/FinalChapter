# Set and Dictionary
"""
marks = {
    "shubham": 92,
    "vaishnavi": 78,
    "rajababu": 68

}

print(marks, type(marks))
print(marks["rajababu"])

# dict methods

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"shubham": 94})
print(marks)

print(marks.get("vaishnavi"))
"""
#Set
name = set()  # empty set
print(type(name))

name = {"shubham, sayali", 12}
num = {12, 56, 12, 67, 44, "shubham"}
print(num, type(num))

# methods

num.add(66)
print(num)

both = name.union(num)
print(both)

both_intersection = name.intersection(num)
print(both_intersection)








