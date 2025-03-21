# File operation I/O

# f = open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\Notes.txt")
# data = f.read()
# print(data)
# f.close()

# Read Operation
# f = open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\FileOperation.txt")
# data = f.read()
# print(data)
# f.close()

# Write Operation

# my_str = "Hey hello sayo... !"
#
# f = open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\FileOperation.txt", "w")
# data = f.write(my_str)
# f.close()

# File Functions.

# readline - It will be print only 1 line.
# readlines - It will be print multiple lines.


# f = open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\FileOperation.txt")
# # data = f.readline()  # It will be print only 1 line.
# data = f.readlines()  # It will be print only 1 line.
# print(data)
# f.close()


# With Statement

with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\FileOperation.txt") as f:
    print(f.read())

# You don't have to explicitly close the file.
