import random

word_list = ['peach', 'pineapple', 'grape', 'pear', 'apple']

word = random.choice(word_list)
print(word)

def ask_for_input():
    while True:
        guess = input("Guess a letter here: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print(f"Oops! '{guess}' is not a valid input. Try again!")
        
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Correct! '{guess}' is in the word!")
        return guess
    else:
        print("Nope! Try again..")
    ask_for_input()

ask_for_input()






