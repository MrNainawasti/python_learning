# Secret Auction Program
from replit import clear 
# we can call clear() to clear the output in the console.
# this is only applicaple in replit.

def add_bidder():
    name = input("What is your name?: ")
    bid = str(input("What's your bid?: $"))
    bidders[name] = bid

from art import logo
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
auction_end = False
while not auction_end:
    add_bidder()
    a = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()
    if a == "no":
       auction_end = True
        
highest_bid  = 0
for bidder in bidders:
    b = int(bidders[bidder])
    if b > highest_bid:
        highest_bid = b
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")

