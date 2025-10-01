import pyttsx3
import os
import pyjokes

"""
import pyjokes

print("Hello World")

joke = pyjokes.get_joke()
print(joke)

# pyjokes is module

# Read Evaluate print loop = repl

print("----------- Printing Jokes------------------")

joke = pyjokes.get_joke()
print(joke)
"""
star = "shubham"

# Practice Set 1
print(f'''Twinkle twinkle little {star}.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')

# speech = pyttsx3.speak("I will call you back")
# print(speech)

# engine = pyttsx3.init()
# engine.say("stop")
# engine.runAndWait()

directory_path = r"F:\Tutorials"
content = os.listdir(directory_path)
print(content)

joke = pyjokes.get_joke()
print(joke)





