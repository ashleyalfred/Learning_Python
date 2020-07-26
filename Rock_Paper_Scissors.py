import random
import time
#create a tuple of choices 
guess = (
    'rock', 
    'paper',
    'scissors'
)

def winner_winner(): 
    

def play_again(): 
    again = input("Do you want to play again? Y/N: ")
    again = again.lower()
    if again == "y" or again == "yes": 
        first_game()

def first_game():
    print("Let's play rock, paper, scissors!!")
    user_choice = input("Enter your choice: ")
    user_choice = user_choice.lower()
    print("Ok, now my turn.")
    print("rolling ... ")
    time.sleep(1)
    ai_choice = random.choices(guess)
    print("I rolled", ai_choice)
    play_again



first_game()
play_again()
