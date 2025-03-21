# problem 01
# 1. Write a program to read a text from given file poems.txt and find out whether it contents word twinkle.


with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\poems.txt") as f:
    my_str = f.read()
    if "twinkle" in my_str:
        print("'twinkle' has been found.")
    else:
        print("not found")
