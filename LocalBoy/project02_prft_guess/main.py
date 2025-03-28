# Project
# perfect guess number.
import random
from random import randint

num = random.randint(1, 100)
a = -1
guesses = 0
while a != num:
    guesses += 1
    a = int(input("Guess the number: "))
    if a > num:
       print("lower number please: ")
    else:
        print("Highr number please")

print(f"you have guesed number:{num}")
