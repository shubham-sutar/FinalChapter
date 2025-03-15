# problem 03
# 3. A spam comment is defined as text contained following content - "make a lot of money", "buy now", "subscribe
# this", "click this"

key1 = "make a lot of money"
key2 = "buy now"
key3 = "subscribe this"
key4 = "click this"

comment = input("Enter your Comment: ")
if comment in key1 or comment in key2 or comment in key3 or comment in key4:
    print("This comment is a spam")
else:
    print("your successfully commented..!!")

