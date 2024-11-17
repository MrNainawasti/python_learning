# NATO Alphabet Project
The NATO phonetic alphabet is a set of standardized pronunciations for letters and numbers used to communicate orally. The user is asked to enter any word and the program converts the user entered word into phonetic code and gives output.

This project is developed using basic concepts of List and Dictionary comprehension.


# List and Dictionary Comprehenson
List Comprehension:

new_list = [new_item for item in list if test]

Dictionary Comprehension:

new_dictionary = {new_key: new_value for (key,value) in dictionary.items() if test}


Using List and Dictionary comprehension in pandas DataFrame:

List Comprehension:

new_list = [new_item for (index,row) in DataFrame.iterrows() if test]

Dictionary Comprehension:

new_dictionary = {new_key: new_value for (index,row) in DataFrame.iterrows() if test}

# Error and Exception Handling
This proect was updated later for errors and exception handling. When the user gives in a string that is other than alphabet, then KeyError occurs and exception handling is used to take care of that.

In Python, there are several built-in Python exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

KeyError: This exception is raised when a key is not found in a dictionary.

ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

# Exception Handling

try: (something that might cause an exception)

except: (do this if there was an exception)

else: (do this if there weren't any exceptions)

finally: (do this no matter what happens)

raise exception_type: (raise your own exception)