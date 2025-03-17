# problem 01
# 1. write a program using a function to find greatest of three numbers.


def greatest_num():
    num1 = int(input("enter first num: "))
    num2 = int(input("enter second num: "))
    num3 = int(input("enter third num: "))
    return max(num1, num2, num3)


sol = greatest_num()
print(f"The greatest number of three is : {sol}")

# def greatest_num(num1, num2, num3):
#     return max(num1, num2, num3)

#sol = greatest_num( 45, 67, 80)
#print(f"The greatest number of three is : {sol}")
