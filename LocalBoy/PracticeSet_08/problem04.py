# problem 04
# 4. Write a recursive function to calculate first n natural numbers.


def natural_num(n):
    if n == 1:  # Base case to stop recursion
        return 1
    return n + natural_num(n - 1)


n = int(input("Enter any num: "))

if n < 1:
    print("Please enter a natural number (n ≥ 1).")
else:
    print(f"The sum of the first {n} natural numbers is {natural_num(n)}")
