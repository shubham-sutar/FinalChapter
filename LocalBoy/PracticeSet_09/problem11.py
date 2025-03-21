# problem 11
# 11. Write a python program to rename a file to "reamed_by_python.txt

file_path = r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\dummy.txt"

with open(file_path, "r") as f:
    content = f.read()

file_path = r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\renamed_by_cose_dummy.txt"
with open(file_path, "w") as f:
    content1 = f.write(content)
