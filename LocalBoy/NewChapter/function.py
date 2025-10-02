# function
"""
name = "shubhamsutar"
print(len(name))  # 12
print(name.endswith("ar"))  # true
print(name.startswith("Sh"))  # false
print(name.capitalize())  # Shubhamsutar

# Escape sequence
name = "shubhamsutar"
name1 = "shubham\nsutar"  # \n - new line
name2 = "shubham\tsutar"  # \t - tab
name3 = "\"shubhamsutar\""  # "shubhamsutar"
name4 = "shubham\\sutar"
print(name4)

# problems

name = input("Enter user name: ")
greet = " good afternoon "
new_User = greet + name
print(new_User)

letter = '''
Dear {name},
You are selected !
{date}
'''
print(letter.replace("{name}", "Shubham").replace("{date}", "02/10/2025"))


name = " My name is shubham  sutar"
# print(name.find("  "))
print(len(name))
print(name.replace("  ", " "))
print(len(name))


letter = "Dear sir, This python course is nice. Thanks!"
print("\"Dear sir,\n\tThis python course is nice.\n\tThanks!\"")

"""
# a = "shubham"
# a[0] = "S"
# print(a)

# list

fruits = ["apple", "mango", "orange", "kiwi", "book", 122, 13.5]
# print(f"There are list of fruits: ", fruits)
fruits[0] = "grapes"
print(fruits)

# fruits[10] = "banana"
# print(fruits)  # index out of bound

print(fruits[0:4])
fruits.append("jack")
print(fruits)

numbers = [12, 22, 1, 33, 4, 90, 0, -1, 4.5]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(7, 69)
print(numbers)

value = numbers.pop(5)
print(value)

numbers.remove(-1)
print(numbers)













