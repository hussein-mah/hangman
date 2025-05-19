

import random

# List of words to choose from
word_list = ["python", "hangman", "developer", "programming", "computer"]
word = random.choice(word_list).lower()
guessed_letters = set()
attempts = 6  # Number of wrong attempts allowed

def display_word():
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

print("Welcome to Hangman!")
while attempts > 0:
    print("\nWord:", display_word())
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.add(guess)
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        attempts -= 1
        print("Incorrect! Attempts left:", attempts)

if attempts == 0:
    print("\nGame over! The correct word was:", word)

