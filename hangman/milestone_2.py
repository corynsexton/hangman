import random

word_list = ['Peach', 'Pineapple', 'Grape', 'Pear', 'Apple']    #List of words for game
print(word_list)

word = random.choice(word_list)                 #Select a word from the list at random
print(word)

guess = input("Guess a letter here: ")          #Ask user to guess a letter in the random word selected
print(guess)

if len(guess) == 1 and guess.isalpha():         #This makes sure the user can only guess one letter and that it is a letter, not a number or character
    print(f"Good guess!")                       #Tells user their guess is valid
else:
    print(f"Oops! {guess} is not a valid input. Try again!")   #Tells user to try again if their guess doesn't meet the requirements