import random
import time
#create a tuple of choices 
guess = (
    'rock', 
    'paper',
    'scissors'
)

def play_again(): 
    again = input("Do you want to play again? Y/N: ")
    again = again.lower()
    if again == "y" or again == "yes": 
        first_game()

def first_game():
    print("Let's play rock, paper, scissors!!")
    ready = input("Enter your choice: ")
    ready = ready.lower()
    if ready == "rock" or ready == "paper" or ready == "scissors": 
        print("Ok, now my turn.")
        time.sleep(1)
        print("rolling ... ")
        time.sleep(1)
        print("I rolled", random.choices(guess))
        play_again



first_game()
play_again()
