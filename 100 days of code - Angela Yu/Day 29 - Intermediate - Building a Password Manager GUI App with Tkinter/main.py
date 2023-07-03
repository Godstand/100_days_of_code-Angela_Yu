from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = "Calibre"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Let's generate a random index for letter, numbers, and symbols
    password = ""
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list_1 = password_letters + password_numbers + password_symbols
    password_list = list(password_list_1)
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered:\n Email: {email}\n Password: {password}\n "
                                           f"Is it okay to save?")
    if len(website) or len(email) or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_ing = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_ing)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password", bg="white")
password_label.grid(column=0, row=3)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="    Generate Password", width=14, bd=0, highlightthickness=0, bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, bd=0, highlightthickness=0, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
