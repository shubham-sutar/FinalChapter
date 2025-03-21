# problem 03
# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. place this
# file in a folder for 13-year old.


# def mult_table():
#     for i in range(2, 21):
#         for j in range(1, 11):
#             print(f"{i} x {j} ={i * j}")


def fun_print():
    with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\problem03.txt", "w") as f:
        for i in range(2, 21):
            for j in range(1, 11):
                f.write(f"{i} x {j} ={i * j}\n")

    print("Multiplication Table successfully printed.")


fun_print()
