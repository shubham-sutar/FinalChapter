# conditionals

age = int(input("Enter your age: "))

if (age > 18) and (age < 25):
    print("your teenager")
elif (age >= 25) and (age < 50):
    print("Your adult")
elif age >= 50:
    print("your ODG")
elif age <= 0:
    print("wrong input")
else:
    print("your child")
