# problem 02
# 2. Write a program to great all person names stores in a list "l" with starts with "s"

l = ["harry", "soham", "sachin", "rahul", "soma", "sayo"]

for name in l:
    if name.startswith("s"):
        print(f"Hello {name}")

