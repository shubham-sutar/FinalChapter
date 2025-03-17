# problem 04
# 4. prime number

num = int(input("Enter a number to check prime or not: "))

for items in range(2, num):
    if num % items == 0:
        print(f"{num} Number is not prime")
        break

else:
    print(f"{num} Number is prime")
