# Password Manager Project
This project is developed using different widgets from Tkinter. The UI allows the user to type-in website, email and password in the entry fields. The credentials entered are saved in a file "data.txt" when the user hits 'Add' button. A pop-up box is generated for confirmation of details entered which is created by using 'MessageBox Widget'. If any of the fields with '*' is left empty then also a pop-up box is generated as a warning. User can press 'Generate password' button to generate a random strong password which is automatically copied to clipboard ready to paste if necessary (using pyperclip).


# MessageBox Widget
Python Tkinter – MessageBox Widget is used to display the message boxes(pop up boxes) in the python applications. The tkinter.messagebox module provides a template base class as well as a variety of convenience methods for commonly used configurations. The message boxes are modal and will return a subset of (True, False, None, OK, CANCEL, YES, NO) based on the user’s selection.

# Pyperclip
Pyperclip provides a cross-platform Python module for copying and pasting text to the clipboard.
To copy text to the clipboard, pass a string to pyperclip.copy(). To paste the text from the clipboard, call pyperclip.paste() and the text will be returned as a string value.
