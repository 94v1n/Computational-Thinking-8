import random

# Pick a word at random
word_list = ["heart"]
hidden_word = random.choice(word_list)
win_or_not = ""

# Guess a word

# First letter (in python, counting starts at 0 not 1)
def guess():
    guess_word = input("ENTER A WORD: ")
    output = ""
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    print(f"Result: {output}")
    if output == "🟩🟩🟩🟩🟩":
        win_or_not = "true"



if win_or_not != "true":
    guess()
else:
    print("You win")
if win_or_not != "true":
    guess()
else:
    print("You win")
if win_or_not != "true":
    guess()
else:
    print("You win")
if win_or_not != "true":
    guess()
else:
    print("You win")
if win_or_not != "true":
    guess()
else:
    print("You win")



# Result
