#simple_treasure_hunt
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You're on a spooky island, embarking on a treasure hunt.\nAs you navigate through the dense, haunted forest,\nyou come to a fork in the path.\nTo the left, you see an ancient,\ngnarled tree with a hollow that seems to whisper secrets.\nTo the right, there's a faint,\nglowing light that flickers like a beacon.\n")
print("To find the treasure, answer this question:\n")
choice1 = str(input('"Do you trust the eerie whispers of the ancient tree on the left,\nor do you follow the mysterious glow on the right?"(left or right): '))
if choice1 == "left":
          print("\n*You decide to trust the eerie whispers of the ancient tree on the left.\nAs you follow the path,\nthe whispers guide you to a wide, dark river. \nhe water flows swiftly, and strange ripples disturb the surface,\nhinting at unseen creatures lurking below.\n")
          print("To continue your quest for the treasure, you must decide:\n")
          choice2 = str(input('"Do you dare to take the plunge and swim through the river,\n potentially finding a quicker path to the treasure?"(swim or wait): '))
          if choice2 == "wait":
                    print("\n*The boat arrives and you cross the river,\nyou come across three imposing doors ahead: one red, one blue, and one yellow.\nEach door exudes an aura of mystery,\nhinting at the secrets they hold within.\n") 
                    print("To proceed in your quest for treasure, you must decide:\n")
                    choice3 = str(input('Which door will you choose:\nthe red, the blue, or the yellow? '))
                    if choice3 == "yellow":
                              print("\nCongratulations! You've chosen wisely.\nYou've found the treasure and emerged victorious in your quest.\nWell done, adventurer!")
                    elif choice3 == "red":
                              print("\nGame Over!! The fiery trap behind the red door\nproves too dangerous to overcome.\nYour quest for treasure ends here, consumed by flames.")
                    elif choice3 == "blue":
                              print("\nGame Over!! The beasts lurking behind the blue door\nprove too formidable to overcome.\nYour quest for treasure ends here,\ndevoured by the creatures of the darkness.")

                    else:
                              print("\nGame over!!")
          else:
                    print("\nGame Over!! You struggle against the unseen force, but it's futile. You've been ensnared by the creatures lurking beneath the surface, and your quest for treasure comes to a premature end.")
                    
else:
          print("\nGame Over!! You have chosen the wrong path. The treasure remains hidden, awaiting the next brave adventurer.")


 
