# File Handling
# How to Read a text, and write into it using python code.

# Function -
# open("file_name", "mode")

# Mode -
# 'r' for reading (default).
# 'w' for writing (create a new file or truncates an existing one)
# 'a' for appending.
# 'b' for binary mode. zoom.exe - binary
# '+' for updating (reading and writing).

# read and write content
# read a file
# reading Entire content: content = file_object.read()
# line = file_object.readline() for single line.
# lines = file_object.readlines() for all lines in a list.
# close the file
"""
file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()
"""

file = open('sample.txt', 'a')
content = file.write("Python is Easy, Happy coding")
file.close()



