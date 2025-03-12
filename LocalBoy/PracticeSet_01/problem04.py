# problem4
# list the directory content by using python code

import os

directory_path = r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\01_Basics"

content = os.listdir(directory_path)

for item in content:
    print(item)
