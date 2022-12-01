import random

class Hangman():                                                            #Class called Hangman

    def __init__ (self, word_list, num_lives = 5):                          #Initializes attributes - uses word_list created and asigns user 5 lives to play        
        self.word = random.choice(word_list)                                #Selects random word from word_list
        self.num_letters = len(self.word)                                   #Number of letters in word selected
        self.num_lives = num_lives                                          #Number of lives player has at start of game
        self.word_list = word_list                                          #List of words to select at random from
        self.list_of_guesses = []                                           #List to store guesses that player has already tried
        self.word_guessed = len(self.word) * ['_']                          #Letters in word to be guessed replaced with '_'
    
    def check_guess(self, guess):                                           #A method to check if the guess is in the word
        guess = guess.lower()                                               #Changes any guesses to lower case

        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")                   #Tells user if guess is in the word
            
            for i, j in enumerate(self.word):                               #Uses enumerate function to look at index and letter in word
                if guess == j:                                              #If guessed letter is same as one in word
                    self.word_guessed[i] = j                                #Changes '_' to letter if in word
                    self.num_letters -= 1                                   #One less letter to guess in word
            print(self.word_guessed)                                        #Shows user word with correct guesses included

        else:
            self.num_lives -= 1                                             #User loses a life if guess is incorrect
            print(f"Sorry, '{guess}' is not in the word") 
            print(f"Guess again. You have {self.num_lives} remaining.")     #Tells user how many lives remaining
        
        self.list_of_guesses.append(guess)                                  #Adds guessed letter to list of guesses


    
    def ask_for_input(self):                                                #A method to ask user to guess and make sure it's valid
        
        guess = input("Guess a letter: ")                                   #Asks user to guess a letter

        if not guess.isalpha() or len(guess) != 1:                          #Makes sure guess is valid
            print(f"Oops! '{guess}' is not a valid input. Try again!")
        elif guess in self.list_of_guesses:                                 #Checks if user has already guessed that letter
            print("You have already guessed this letter! Try again..")
        else:
            self.check_guess(guess)                                         #Takes guess and sends it to check if in word      

                          

def play_game(word_list):                                                   
    game = Hangman(word_list, num_lives = 5)                                #Calls Hangman class
    
    while True:
        if game.num_lives == 0:                                             #Tells user they lose if they have 0 lives
            print("You lost!")
            break                                                           #Ends game if user runs out of lives
        elif game.num_letters > 0:                                          #Allows user to guess again if they have lives
            game.ask_for_input()
        else:
            print("Congratualations! You win!")                             #Tells user they win once all letters are guessed within 5 lives
            break                                                           #Ends game once word is guessed


word_list = ['pineapple', 'pear', 'peach', 'apple', 'kiwi', 'grape']        #List of words to choose randomly from
play_game(word_list)
