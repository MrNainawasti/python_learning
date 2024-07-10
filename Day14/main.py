# higher lower game
import random

from replit import clear

import art
from game_data import data


def choose_details():
    details = random.choice(data)
    name = details["name"]
    description = details["description"]
    country = details["country"]
    followers = details["follower_count"]
    return name, description, country, followers

def compare(choice, A1, B2):
    if choice == "A" and A1 > B2 or choice == "B" and B2 > A1:
        return "correct"
    else:
        return "incorrect"

def game_start():
    print(art.logo)
    name1, description1, country1, followers1 = choose_details()
    print(f"Compare A: {name1}, {description1}, {country1} ")
    def option2():
        score = 0
        game_over = False
        while not game_over:
            name2, description2, country2, followers2 = choose_details()
            if name2 != name1: 
                print(art.vs)
                print(f"Against B: {name2}, {description2}, {country2} ")
                user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
                result = compare(user_choice, followers1, followers2)
                if result == "correct":
                    score += 1
                    clear()
                    print(art.logo)
                    print(f"You're right! Current score: {score}")
                    print(f"Compare A: {name2}, {description2}, {country2} ")
                else:
                    game_over = True
                    clear()
                    print(art.logo)
                    print(f"Wrong answer! Final score: {score}")
                    play = input("\ndo you want to play again?(y/n): ").lower()
                    if play == "y":
                        clear()
                        game_start()        
            else:
                option2()
                
    option2()
    
game_start() 
