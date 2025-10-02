# tuples
# immutable
# denoted by ()
"""
numbers = ()
print(type(numbers)) # empty tuple

numbers = (1)
print(type(numbers))  # int
numbers = (1,)
print(type(numbers))  # tuple

tup = ("mee", 12, 67, -1, True)
tup[2] = 33  # immutable
print(tup)

# tuple methods
tup = ("mee", 12, 67, -1, True, -1, 0, -1)
repeat = tup.count(-1)
print(repeat)

fruits = []

my_fruits = input("Enter fruits name: ")
fruits.append(my_fruits)
print(fruits)


marks = []
marks_obtain = int(input("enter marks of stud: "))
marks.append(marks_obtain)

marks.sort()
print(marks)

marks = []
obtained_marks1 = int(input("Enter marks of student: "))
marks.append(obtained_marks1)
obtained_marks2 = int(input("Enter marks of student: "))
marks.append(obtained_marks2)
obtained_marks3 = int(input("Enter marks of student: "))
marks.append(obtained_marks3)

marks.sort()
print(marks)


name = (12, 45, 78)
name[0] = "shubham"
print(name)


listing = [21, 55, 78, 9]
# sum = listing[0]+listing[1]+listing[2]+listing[3]

print(sum(listing))
"""

tuple_exm = (0, 12, 23, 0, 45, 67, 88, 0)

total_count = tuple_exm.count(0)
print(total_count)


















