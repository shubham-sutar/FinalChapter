# problem 03
# 03. Write a program to detect double space in a string.

my_string = "Sayali your very beautiful girl"
print(my_string.find("  "))

# output occurs positive integer then double space found.
# output occurs negative -1 then double space not found.

story = '''
    Shubham was a curious boy who loved solving puzzles and mysteries. One day, he found an old, dusty book in his grandfather’s attic. As he flipped through its pages, he discovered a hidden map leading to a secret cave. Excited, he gathered his friends and set out on an adventure. After hours of searching, they found the cave hidden behind a waterfall. Inside, they discovered ancient coins and a letter from a lost explorer. The letter revealed the explorer’s dream of sharing his treasure with the world. Inspired, Shubham decided to donate the coins to a museum. His story spread, and he became a young hero in his town. Encouraged by his success, he continued exploring new places. His love for adventure never faded, and he dreamed of becoming a great archaeologist one day.
'''
index = story.lower().find("shubham")
updated_story = story.replace("Shubham", "Ajay")

print(index)
print(updated_story)
