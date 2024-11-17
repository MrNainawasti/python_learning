import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_code = { row.letter: row.code for (index,row) in data.iterrows() }


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    
    try:
        phonetic_code = [ letter_code[letter] for letter in user_word ]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(phonetic_code)


generate_phonetic()

