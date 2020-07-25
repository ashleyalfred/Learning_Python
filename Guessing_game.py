import random
#create a tuple of clues 
clues = (
    "Here's a clue: it's less than 5 but greater than 0!", 
    "Here's a clue: it's greater than 2 but less than 8!",
    "Here's a clue: it's much smaller than 10!",
    "Here's a clue, it's not analogous with A, I, O or U"
)

def answer_correct():
    print("Your answer is correct! Good for you!")


def answer_incorrect():
    print("Incorrect!")
    print(random.choices(clues))
    play_again()
    

def play_again():
    while True: 
        try: 
            print("Guess the secret number!")
            user_number = int(input("Enter a whole number from 1-10: "))
            if user_number >= 1 and user_number <= 10:
                break
        except: 
            pass
    if user_number == 4:
        answer_correct()
    else:
        answer_incorrect()


play_again()
answer = input("Do you want to play again? Y/N:  ")
if answer == "Y":
    play_again()
