# problem 07
# 7. Write a python function to remove a given word from a list ad strip it at the same time.

def remove_and_strip(lst, word):
    new_list = []
    for item in lst:
        stripped_item = item.strip()
        if stripped_item != word:
            new_list.append(stripped_item)
    return new_list


# Example usage:
words = ["  apple  ", "banana", "  orange  ", "apple", "  mango "]
word_to_remove = "apple"

result = remove_and_strip(words, word_to_remove)
print(result)
