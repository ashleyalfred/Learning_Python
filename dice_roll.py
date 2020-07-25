import random
import time

def dice_roll():   
    print("Rolling ... ")
    time.sleep(1)
    print("You rolled a", random.randint(0,9))
    time.sleep(1)
    print("Ok, now it's my turn!")
    time.sleep(1)
    print("Rolling ... ")
    time.sleep(1)
    print("I rolled a", random.randint(0,9))
    again = input("Do you want to play again? Y/N: ")
    if again == "Y" or again == "y" or again == "yes" or again == "Yes":
        dice_roll()
        

answer = input("Do you want to roll the dice? Y/N: ")
if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
    dice_roll()
