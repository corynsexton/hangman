# Hangman
In this project, I am re-creating the famous game of Hangman. For those of you who don't know, Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attenpts, guessing a letter at a time. This project is an implementation of this, where the computer generates a word at random and the user tries to guess it.

---

## Milestone 1
Some technologies used in thie making of this game are Python, Git, GitHub, random import, user input, if, elif and els statements, while and for loops, functions, classes and methods.c

---

## Milestone 2
I started by using some basics in Python to create a list of words and using the 'random' package to select a word at random from this list for the user to guess.
I then used the input function to ask the user to guess a letter.

Following this, I created an 'if' statement to ensure the guess was valid. For example, a number, character or two letters would not be valid guesses. One single alphabetical letter would class as a valid guess. I did this by ensuring the guess was == 1 character and by using the .isalpha() function.

<img width="531" alt="milestone_2" src="https://user-images.githubusercontent.com/117574774/204358053-3cdfa5ae-1fe6-444c-8223-a409d2641c64.png">

---
## Milestone 3
Milestone 3 is where I created two functions - one to ask the user to guess a valid letter, and the other to check if the user's guess is in the word.
In the ask_for_input function, I used my if, else statement code from Milestone 2 and put it in a 'while True' loop to allow the guess to go ahead as long as it is valid. If it meets the requirements, I have used 'break' to end the loop. If not, it will tell the user the guess is invalid and allow them guess again.
In the check_guess function, I have passed in the user's guess from the input function as an argument and this will check if their guess is in the word. I have used print statements to tell the user if the guess is in the word or not. If it is, my code returns their guess, If it is not, it tells the user to try again and runs the ask_for_input function again.
To finish off, I have called the ask_for_input function to allow the user to keep guessing until they find a letter in the word.
Below is an example of what my code returns in the terminal if the guess is invalid (a number/more than one letter), not in the word and in the word:



---
## Milestone 4
In this Milestone, I have created a class for the game and have used the functions that I created in Milestone 3 as methods for this game.
I started by initializing the attributes of the class by using the __init__ method and passing in the word list created and the number of lives as parameters.



I have used my check_guess function created in Milestone 3 to check if the guess is in the word and I have also added a few elements such as the .lower() method which is built into Python to ensure the guess is lower case. I have also used the enumerate function within a for loop to allow the code to iterate through each letter within the random word selected. If a letter is in the word, my code will replace the unknown '_' with the letter guessed and reduce the number of letters remaining to be guessed. If the guess is not in the word, it will reduce the number of lives the user has remaining.



Again, in my ask_for_input method, I have used the function cerated in Milestone 3 and added an 'elif' statement to it. The elif statement checks if the user has already guessed this letter and prints out a message telling them if so. If not, my else statement will add the guess to the list of guesses and send the letter to be checked with the check_guess method mentioned above.



I finish off by asigning the Hangman class to a variable called 'game' and ask the user for input to begin.



---
## Milestone 5
Milestone 5 is all about bringing the game together by using the class created in Milestone 4.
I created a function called play_game to ensure the game ends correctly, with the user winning if they guess all of the letters in the word, or losing if they run out of lives.
The first thing I do in this function is put in the word list as a parameter, call the Hangman class and asign it to a variable called 'game'. I have created a loop within this function which tells the user if they have won or lost. A print statement is used to tell the user they have lost once their lives == 0, followed by 'break' which ends the loop. If the user still has 1 or more lives remaining, the loop will continue and will allow the user to guess again When there are no more letters to guess, the game will then know the user has found all of the letters and will tell the user they have won the game, ending with 'break' to end the loop.
Finally, outside of the function, I call the play_game function to begin the game.





