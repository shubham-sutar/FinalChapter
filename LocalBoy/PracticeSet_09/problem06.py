# problem 06
# 6. write a program to mine a log file and find out whether it contains 'python'

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\problem06.html", "r") as f:
    content = f.read()

if "python" in content:
    print("Yes python has founded")
else:
    print("python is not in file.")

