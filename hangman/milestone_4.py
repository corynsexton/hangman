import random

word_list = ['peach', 'pineapple', 'grape', 'pear', 'apple']

class Hangman():                                                                    #Creates a class for game
    def __init__ (self, word_list, num_lives = 5):                                  #Initializes attributes of class
        self.word_list = word_list                                                  #List of words
        self.word = random.choice(word_list)                                        #Random word from list to be guessed
        self.num_lives = num_lives                                                  #Number of lives player has at start of game  
        self.word_guessed = len(self.word) * ['_']                                  #Letters in word to be guessed replaced with '_'
        self.num_letters = len(self.word)                                           #Number of letters in word yet to be guessed
        self.list_of_guesses = []                                                   #List to store guesses that player has already tried
    
    def check_guess(self, guess):
        guess = guess.lower()                                                       #Ensures the letter is lower case

        if guess in self.word:
            print(f"Correct! '{guess}' is in the word!")

            for i, j in enumerate(self.word):                                       #Looks at the index and letter of our word
                if guess == j:                                                      #If guessed letter is the same as one in word
                    self.word_guessed[i] = j                                        #Enters guessed letter in word instead of '_'
                    self.num_letters -= 1                                           #One less letter to guess in word
            print(self.word_guessed)                                                #Prints word with guessed letter in it

        else:
            self.num_lives -= 1                                                     #If incorrect guess, user loses a life
            print(f"Nope! You have {self.num_lives} lives remaining. Try again..")
    

    def ask_for_input(self):
        while True:                                         
            guess = input("Guess a letter here: ")                                  #Asks user for input
        
            if not guess.isalpha() or len(guess) != 1:                              #Validates the guess
                print("Invalid guess. Please enter a single alphabetical letter.")

            elif guess in self.list_of_guesses:                                     #Checks user hasn't already guessed that letter
                print("Guess again - You already tried that letter!")

            else:
                self.list_of_guesses.append(guess)                                  #Adds guess to list of guesses
                self.check_guess(guess)                                             #Checks if guess is in the word
                

game = Hangman(word_list, num_lives=5)                                              #Asigns Hangman class to variable 'game'
game.ask_for_input()                                                                #Calls ask_for_input method
        
                 
                             
