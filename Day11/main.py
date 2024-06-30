# simple_blackjack_game
import random
from replit import clear
from art import logo
def deal_card():
    card = random.choice(cards)
    return card

def current_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return score

def compare(my_score, bot_score):
    if my_score > 21:
        return "\nYou went over. YOU LOSE!!"
    elif my_score == bot_score:
        return "\nDRAW!"
    elif bot_score == 0:
        return "\nThe opponent has BLACKJACK! YOU LOSE!!"
    elif my_score == 0:
        return "\nCONGRATULATIONS!! you win with a BLACKJACK!"
    elif bot_score > 21:
        return "\nOpponent went over. YOU WIN!!"
    elif my_score > bot_score:
        return "\nYOU WIN!!"
    else:
        return "\nYOU LOSE!!"



cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
score = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    print(logo)
    game_over = False
    my_cards = []
    bot_cards = []
    my_points = []
    bot_points = []
    my_cards = my_cards + [deal_card(), deal_card()]
    bot_cards = bot_cards + [deal_card(), deal_card()]
    for card in my_cards:
        a = cards.index(card)
        my_points = my_points + [score[a]]
    for card in bot_cards:
        a = cards.index(card)
        bot_points = bot_points + [score[a]]
    while not game_over:
        my_score = current_score(my_points)
        bot_score = current_score(bot_points)

        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {bot_cards[0]}")

        if my_score == 0 or bot_score == 0 or my_score > 21:
            game_over = True
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if new_card == "y":
                my_cards.append(deal_card())
                b = cards.index(my_cards[-1])
                my_points.append(score[b])
            else:
                game_over = True

    while bot_score != 0 and bot_score < 17:
        bot_cards.append(deal_card())
        b = cards.index(bot_cards[-1])
        bot_points.append(score[b])
        bot_score = current_score(bot_points)

    print("______________________________________________")
    print(f"Your final hand: {my_cards}, final score: {my_score}") 
    print(f"Computer's final hand: {bot_cards}, final score: {bot_score}")    
    print(compare(my_score, bot_score))
    if input("\nDo you want to play another round?(y/n): ") == "y":
        clear()
        blackjack()

play = input("Do you want to play a game of blackjack?(y/n): ")
if play == "y": 
    clear()
    blackjack()
    
