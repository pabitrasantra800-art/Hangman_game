import random

words = ["apple", "train", "chair", "house", "plane"]

word = random.choice(words)
chances = 6

print("Guess the word")

while chances > 0:
    guess = input("Enter your word: ")

    if guess == word:
        print("Correct! You won")
        break
    else:
        chances -= 1
        print("Wrong guess. Chances left:", chances)

if chances == 0:
    print("You lost. The word was:", word)
