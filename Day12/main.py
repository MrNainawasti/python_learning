#Number Guessing Game 
import random
from replit import clear
from art import logo

def difficulty_level():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        tries = 10
    else:
        tries = 5 
    return tries    

def number_guess(guess, a):
    if guess == a:
        return f"\nCongratulations!! \nYou got it!! The answer is {a}."
    elif guess < a:
        return "\nToo Low. \nGuess again!\n"
    else:
        return "\nToo High. \nGuess again!\n"


def game():
    clear()
    print(logo)
    print("WELCOME TO THE NUMBER GUESSING GAME!!") 
    attempts = difficulty_level()
    print(f'''\nI'm thinking a number between 1 and 100. \nYou have {attempts} attempts to guess the number!''')
    a = random.randint(1, 100)
    game_over = False
    while attempts != 0 and not game_over:
        guess = int(input("make a guess: "))
        result = number_guess(guess, a) 
        print(result)
        if guess == a:
            game_over = True    
        else:
            attempts -= 1
            print(f"{attempts} attempts remaining...")
            if attempts == 0:
                print(f"\nGame over!! You are out of attempt!! \nThe right answer is {a}")
                game_over = True
        if game_over :
            retry = input("\nDo you want to play again?(y/n): ")
            if retry == "y" or retry == "":
                game()
            else:
                clear()


game()
