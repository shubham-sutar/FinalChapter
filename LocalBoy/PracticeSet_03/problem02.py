# problem 02
# 2. Write a Program to fill in a letter template given below with name and date.

letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''

print(letter.replace("<|Name|>", "Sayali").replace("<|Date|>", "13/03/2025"))
