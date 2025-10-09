# Write a python program to input eight numbers from the user and display all unique numbers (once)

marks = []
sub_mark1 = int(input("enter marks: "))
marks.append(sub_mark1)
sub_mark2 = int(input("enter marks: "))
marks.append(sub_mark2)
sub_mark3 = int(input("enter marks: "))
marks.append(sub_mark3)
sub_mark4 = int(input("enter marks: "))
marks.append(sub_mark4)

print(marks)
total = set(marks)
print(total)
print(len(total))

