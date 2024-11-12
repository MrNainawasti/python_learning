import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_code = { row.letter: row.code for (index,row) in data.iterrows() }

user_word = input("Enter a word: ").upper()

phonetic_code = [ letter_code[letter] for letter in user_word ]

print(phonetic_code)

