import random
from wordlist import words
import string

# selecting words without '-' or ' '
def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


# hangman method
def hangman():
    word = get_valid_word().upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # saves set of words used for Guessing

    # iterating till all letters are found
    while len(word_letters) > 0:
        # to show the letters used by the user
        print(" You have used these letter: ", ' '.join(used_letters))

        # showing the progress of guessing ( ie W - R D)
        list_of_words = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(list_of_words))

        # accepting letter from user
        guessing_letter = input("Guess your letter: ").upper()

        if guessing_letter not in alphabet:
            print(" Invalid Character, Try again")

        elif guessing_letter in used_letters:
            print("Opps! you have already guessed that letter....")

        else:
            used_letters.add(guessing_letter)
            if guessing_letter in word_letters:
                word_letters.remove(guessing_letter)

    print("\n", word)
    print(" Congrats! you have Found your word")


hangman()
