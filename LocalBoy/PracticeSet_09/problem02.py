# problem 02
# 2. The game function in a program lets a user play a game and returns score assign integer. You need to read file
# "Hi-score.txt". Which is either blank or contains the previous Hi-score. You need to write a program to update the
# hi-score whenever the game() breaks the hi score.

# score = int(input("Enter a score: "))
# break_score = 0
#
#
# def game(score):
#     if break_score < score:
#         with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\hi_score.txt", "w") as f:
#             f.write(str(score))
#             return f"new breaking score {score}"
#     else:
#         print("Score is not breaking.. !!")
#
#
# new_score = game(score)
# print(new_score)

score = int(input("Enter a score: "))

# Read previous high score from file
try:
    with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\hi_score.txt", "r") as f:
        content = f.read().strip()
        break_score = int(content) if content.isdigit() else 0
except FileNotFoundError:
    break_score = 0  # If file doesn't exist, assume high score is 0


def game(score):
    global break_score
    if score > break_score:
        with open(r"C:\Users\Admin\PycharmProjects\FinalChapter\LocalBoy\PracticeSet_09\hi_score.txt", "w") as f:
            f.write(str(score))
        return f"New breaking score {score}"
    else:
        return "Score is not breaking.. !!"


new_score = game(score)
print(new_score)
