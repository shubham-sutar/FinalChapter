# problem 06
# 6. Write a python function which coverts inches to cms.


def convert(inch):
    return inch * 2.54


inch = float(input("Enter inch to convert cms: "))
cms = convert(inch)

print(f"{inch} inch converted to {cms} cms")
