#choice randomly picks something from a tuple (any sequence)
from random import choice
from time import sleep
#tuple of choices 
choices = ('rock', 'paper', 'scissors')

#create a class to represent a player with a name
class Player():
    def __init__(self, name):
        self.score = 0
        self.name = name 
    
    #create a method to get the users choice 
    def get_choice(self):
        while True:
            user_choice = input(f"{self.name}, enter your choice (rock, paper, scissors): ").lower()
            if user_choice in choices:
                self.current_choice = user_choice
                break

    def print_current_choice(self):
        print(f"{self.name} picked {self.current_choice}")

    def did_tie(self, other_player):
        return self.current_choice == other_player.current_choice

    def did_win(self, other_player):
        return (
            (self.current_choice == 'rock' and other_player.current_choice == 'scissors')
            or (self.current_choice == 'paper' and other_player.current_choice == 'rock')
            or (self.current_choice == 'scissors' and other_player.current_choice == 'paper')
        )

    def increment_score(self):
        self.score = self.score + 1

#subclass (or child class) of player (or parent)
#it takes the properties/methods from the parent (score, setting the name) 
#don't forget you still have to define init self!
class AIPlayer(Player):
    def __init__(self):
        Player.__init__(self, "AI")

    #overrides get_choices from the parent (making it a random "choice" with the tupple "choices")
    def get_choice(self):
        self.current_choice = choice(choices)

def winner(player1, playe2): 
    if player1.did_tie(player2):
        return None
    elif player1.did_win(player2):
        return player1
    else:
        return player2

def print_scores(player1, player2): 
    print(f"{player1.name}'s score is now {player1.score}")
    print(f"{player2.name}'s score is now {player2.score}")


def single_round(player1, player2):
    player1.get_choice()
    player1.print_current_choice()
    sleep(.5)

    player2.get_choice()
    player2.print_current_choice()
    sleep(.5)

    winning_player = winner(player1, player2)
    if winning_player is None: 
        print("Tie!")
    else: 
        print(f"{winning_player.name} won!!")
        winning_player.increment_score()
    sleep(.5)
    print_scores(player1, player2)

def multiple_rounds(player1, player2):
    #play as many rounds as you want until you tell it to stop 
    # calling single_round(player1, player2)
    while True: 
        single_round(player1, player2)
        answer = input("Do you want to play again? Y/N: ").lower()
        if answer not in ("y", "yes", "ya", "yeah", "yup"):
            break


        
#calling (instantiating) the class "Player" and naming it "Ashley"
player1 = Player(input ("Enter your name: "))
#doing the same with the child class AIPlayer
player2 = AIPlayer()
multiple_rounds(player1, player2)



