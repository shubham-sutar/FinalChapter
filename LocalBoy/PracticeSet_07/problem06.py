# problem 06
# 6. factorial number

# 4 = 4 x 3 x 2 x 1.


num = int(input("Enter a number: "))

fact = 1
for item in range(1, num + 1):
    fact = item * fact
print(fact)
