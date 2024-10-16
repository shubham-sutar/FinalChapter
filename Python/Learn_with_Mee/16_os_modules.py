# Os Module
# Os Module use to interact with the operating system
# get working directory, change dir, file exists, filename, size file, env.

import os
print(os.name)  # nt
print(os.getcwd())  # get working directory

# os.mkdir("TextFiles")
size = os.path.getsize('sample.txt')
print(size)

# list all directories
all_dir = os.listdir(r"C:\Users\Admin\PycharmProjects\FinalChapter\Python\Learn_with_Mee")
print(all_dir)



