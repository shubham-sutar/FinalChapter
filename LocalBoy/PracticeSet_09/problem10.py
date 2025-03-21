# problem 10
# 10. write a program to wipe out the content of a file using python.

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\problem10.txt", "w") as f:
    content = f.writelines("")

print("problem10.txt presenting successfully wipe out !!")
