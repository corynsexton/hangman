import random

word_list = ['peach', 'pineapple', 'grape', 'pear', 'apple']    #List of words for game    

word = random.choice(word_list)                                 #Selects a word from the list at random                                

guess = input("Guess a letter: ")                               #Asks user to guess a letter in the random word selected                       


if len(guess) == 1 and guess.isalpha():                         #Makes sure the user can only guess one letter and that it is a letter, not a number or character
    print(f"Good guess!")                                       #Tells user to try again if their guess doesn't meet the requirements                                                                        
else:
    print(f"Oops! '{guess}' is not a valid input. Try again!")   