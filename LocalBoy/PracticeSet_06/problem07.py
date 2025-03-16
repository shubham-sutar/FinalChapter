# problem 07
# 7. Write a program to find out whether is post is talking about Harry or not.

user_post = input("Write a post: ")

if "Harry".lower() in user_post.lower():
    print("Post is talking about harry")
else:
    print("post is not talking about harry.")

