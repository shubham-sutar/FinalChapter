# problem 08
# 8. write a program to copy of a file. this.txt

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\this.txt", "r") as f:
    content = f.read()

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\this_copy.txt", "w") as f:
    f.write(content)
    