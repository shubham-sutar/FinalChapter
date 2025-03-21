# problem 05
# 05 censor a word of list

words = ["ganda", "bad"]

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\problem05.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\problem05.txt", "w") as f:
    f.write(content)
