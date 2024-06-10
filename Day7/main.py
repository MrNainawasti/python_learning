# main module
import random
import hangman_arts
import hangman_words

print(hangman_arts.logo)
print(hangman_arts.stages[6])
lives = 6
chosen_word = random.choice(hangman_words.word_list).upper()
letter_list = [*chosen_word]

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")
print(" ".join(display))

# Check guessed letter
end_of_game = False
while not end_of_game:
    x = 0
    guess = input("Guess a letter: ").upper()
    for letter in chosen_word:
        if letter.upper() == guess:
            display[x] = guess
            x += 1
        else:
            x += 1

    if guess not in letter_list:
        lives -= 1
        print(hangman_arts.stages[lives])
        print(" ".join(display))
        # Check lives
        if lives == 0:
            end_of_game = True
            print("Correct answer is:")
            print(" ".join(chosen_word))
            print("You lose!!")
        
    else:
        print(hangman_arts.stages[lives])
        print(" ".join(display))

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!!")


