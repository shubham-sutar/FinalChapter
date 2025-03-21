# problem 09
# 9. write a program whether check file09_one.txt and file09_two.txt present content are equal or not.

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\file09_one.txt", "r") as f:
    content1 = f.readlines()

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\file09_two.txt", "r") as f:
    content2 = f.readlines()

if content1 == content2:
    print("both files presenting content same")
else:
    print("both file presenting content is not same.")
