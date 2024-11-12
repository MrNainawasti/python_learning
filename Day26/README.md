# NATO Alphabet Project
The NATO phonetic alphabet is a set of standardized pronunciations for letters and numbers used to communicate orally.

This project is developed using basic concepts of List and Dictionary comprehension. 

List Comprehension:
    new_list = [new_item for item in list if test]

Dictionary Comprehension:
    new_dictionary = {new_key: new_value for (key,value) in dictionary.items() if test}



# Using List and Dictionary comprehension in pandas DataFrame:

List Comprehension:
    new_list = [new_item for (index,row) in DataFrame.iterrows() if test]

Dictionary Comprehension:
    new_dictionary = {new_key: new_value for (index,row) in DataFrame.iterrows() if test}