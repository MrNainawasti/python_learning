PLACEHOLDER = "[name]"

with open ("./Input/Names/invited_names.txt", mode="r" ) as names_file:
    names = names_file.readlines()

with open ("./Input/Letters/starting_letter.txt", mode="r" ) as sample:
    file = sample.read()
    for name in names:
        stripped_name = name.strip()
        letter = file.replace(PLACEHOLDER, stripped_name)
        with open (f"../__MACOSX/Mail Merge Project Start/Output/ReadyToSend/letter_to_{stripped_name}.docs", mode="w") as letters:
            letters.write(letter)
        


