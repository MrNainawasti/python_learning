from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    
    shuffle(password_list)
    
    password = "".join(password_list)
    
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().title()
    email = email_entry.get()
    password = pw_entry.get()
    
    new_data = {
        website: {
            "email": email,
            "password": password
        }
        }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="website and password fields cannot be left empty!")
    
    else:
        is_ok = messagebox.askyesno(title="Confirm Data", message=f"confirm the entered data:\nWebsite: {website}\nPassword: {password}" )
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # saving data by creating a file
                    json.dump(new_data, data_file, indent=4)        
            
            else:
                # Updating old data in new data
                data.update(new_data)
            
                with open("data.json", mode="w") as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            
            finally:
                website_entry.delete(0, END)
                pw_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, "example@gmail.com")


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showinfo(title="Oops!", message="Enter website name to search.")
        
    else:    
        try:
            with open("data.json", mode="r") as data_file:
                read_data = json.load(data_file)
                saved_data = read_data[website]
                email = saved_data["email"]
                password = saved_data["password"]
                messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        
        except FileNotFoundError:
            messagebox.showinfo(title="Oops!", message= f"Sorry, no data found on {website}.")
        
        except KeyError:
            messagebox.showinfo(title="Oops!", message= f"Sorry, no data found on {website}.")
        
        else:
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 60, pady= 60)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=40)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

# buttons
pw_button = Button(text="Generate Password", command=generate_pw)
pw_button.grid(row=3, column=2)

add_button = Button(text="Add", command= save_data, width=36)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search_data, width= 14)
search_button.grid(row=1, column=2)


window.mainloop()