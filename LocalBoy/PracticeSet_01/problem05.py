# problem 5
# use comments and multi comments in code

import os

# path of directory
directory_path = r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\01_Basics"

# content
content = os.listdir(directory_path)

# for loop
for item in content:
    print(item)
