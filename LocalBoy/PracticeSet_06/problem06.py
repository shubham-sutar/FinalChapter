# problem 06
# 6. Write a program to calculate a grade of a student from his marks from the following scheme.
"""
90 - 100 = Ex
80 - 90 = A
70 - 80 = B
60 - 70 = C
50 - 60 = D
<50 = Fail
"""

stud_percentage = int(input("Enter your Percentage: "))
if stud_percentage >= 90 and stud_percentage <= 100:
    print("you passed, and your grade is 'EX'")
elif stud_percentage >= 80 and stud_percentage <= 90:
    print("you passed, and your grade is 'A'")
elif stud_percentage >= 70 and stud_percentage <= 80:
    print("you passed, and your grade is 'B'")
elif stud_percentage >= 60 and stud_percentage <= 70:
    print("you passed, and your grade is 'C'")
elif stud_percentage >= 50 and stud_percentage <= 60:
    print("you passed, and your grade is 'D'")
elif stud_percentage < 50:
    print("you are Failed")
else:
    print("you Entered Invalid Percentage")

