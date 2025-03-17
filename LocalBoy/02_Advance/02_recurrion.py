'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n * factorial(n-1)
'''


def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {fact(n)}")
