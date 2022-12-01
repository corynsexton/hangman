import random

word_list = ['peach', 'pineapple', 'grape', 'pear', 'apple']                #List of words for game 

word = random.choice(word_list)                                             #Selects a word from the list at random

def ask_for_input():                                                        #Creating a function to ask the user to guess a letter
    while True:                                                             #A loop which runs while a letter guessed is valid
        guess = input("Guess a letter here: ")                              
        if len(guess) == 1 and guess.isalpha():
            break                                                           #Stops the loop running once a valid letter is entered
        else:                                       
            print(f"Oops! '{guess}' is not a valid input. Try again!")      #Tells the user to guess again if invalid guess 
        
    check_guess(guess)

def check_guess(guess):                                                     #Creating a function to check if the guess is in the word                                                  
    if guess in word:
        print(f"Correct! '{guess}' is in the word!")                        #Tells the user the guess is correct if it is in the word
        return guess                                                        #This will return the guess
    else:
        print("Nope! Try again..")                                          #Tells the user to guess again if letter is not in the word
    ask_for_input()

ask_for_input()                                                             #Calls the ask_for_input function again






