# factorial program

num = int(input("Enter the Number:"))
i = 0
fact = 1

for i in range(num, i, -1):
    fact = fact * i

print(f"Factorial of {num} is : {fact}")
