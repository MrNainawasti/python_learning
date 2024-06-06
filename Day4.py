#rock_paper_scissors_game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rock, Paper, Scissors...Shoot!!")
player = int(input("What do you choose?(0 for rock, 1 for paper, 2 for scissors): "))
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)

computer = random.randint(0, 2)
if computer == 0:
    print(f"computer chose:\n{rock}")
elif computer == 1:
    print(f"computer chose:\n{paper}")
elif computer == 2:
    print(f"computer chose:\n{scissors}")

if player == computer:
    print("Draw!!")
elif player == 0 and computer == 1:
    print("You lost!!")
elif player == 0 and computer == 2:
    print("You won!!")
elif player == 1 and computer == 0:
    print("You won!!")
elif player == 1 and computer == 2:
    print("You lost!!")
elif player == 2 and computer == 0:
    print("You lost!!")
elif player == 2 and computer == 1:
    print("You won!!")
    


