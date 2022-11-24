import random

class Hangman():

    def __init__ (self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.word_guessed = len(self.word) * ['_']
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")
            
            for i, j in enumerate(self.word):
                if guess == j:
                    self.word_guessed[i] = j        
                    self.num_letters -= 1
            print(self.word_guessed)

        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word") 
            print(f"Guess again. You have {self.num_lives} remaining.")
        
        self.list_of_guesses.append(guess)


    
    def ask_for_input(self):
        
        guess = input("Guess a letter: ")

        if not guess.isalpha() or len(guess) != 1:
            print(f"Oops! '{guess}' is not a valid input. Try again!")
        elif guess in self.list_of_guesses:
            print("You have already guessed this letter! Try again..")
        else:
            self.check_guess(guess)         

                          

def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)
    
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratualations! You win!")
            break


word_list = ['entertainment']
play_game(word_list)
