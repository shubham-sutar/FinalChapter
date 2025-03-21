#find  line number

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\problem07.html", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"yes python present in line no : {lineno}")
        break
    lineno = lineno + 1
else:
    print("no python is not present")