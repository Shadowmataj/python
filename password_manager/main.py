import json
from re import search
from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_creator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().title()
    email= email_username_entry.get()
    password = password_entry.get()

    json_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password)== 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(json_data, data_file, indent=4)
        else:
            data.update(json_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No data file found.")
    else:
        if website in data:
            info = data[website]
            email = info["email"]
            password = info["password"]
            messagebox.showinfo(title=f"{website} Account info", message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showerror(title="ERROR", message=f"{website} website has no register.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width=200, height=200)
logo_image = PhotoImage(file = "logo.png")
window.iconphoto(True, logo_image)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=1, row= 0)

#-----------------Labels-------------------------- #
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#-----------------Inputs-------------------------- #
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)

email_username_entry = Entry(width=54)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "christianmataj1@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

#-----------------Button-------------------------- #
generate_button = Button(text="Generate Password", width=15,  command=password_creator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=46, command=save_data)
add_button.grid(column=1, row=4, columnspan= 2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()