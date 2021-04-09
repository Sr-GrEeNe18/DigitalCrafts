
import random
lives = 9
words = ["rain", "clouds", "storm", "umbrella"]
guess = ("word")
secret_word = random.choice(words)

clue = []
for x in secret_word:
    clue.append('-')
# clue = "_" * len(secret_word) ["?, ?, ?, ?, ?"

print(secret_word)
def update_clue(guessed_letter):

    index = 0

    while index  < len(secret_word):

        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter

        index += 1


while lives > 0:

    print(clue)
    print(f"you have {lives} remaining")

    if guess in secret_word :
        update_clue(guess)

    else:
        lives -= 1

def game(secret_word):
    return f"Guess the word {x} ."

Guess = input("what word would you choose?")



