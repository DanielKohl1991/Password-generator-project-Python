from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as file:
            # reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data file found")
    else:
        if website in data:
            search_data_email = data[website]["email"]
            search_data_pw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {search_data_email}\n Password: {search_data_pw}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    #for char in range(nr_symbols):
    # password_list += random.choice(symbols)
    #
    #for char in range(nr_numbers):
    #  password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_pw.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_text():
    website = entry_website.get()
    username = entry_username.get()
    pw = entry_pw.get()
    new_data = {
        website: {
            "email": username,
            "password": pw,
        }
    }
    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title="oops", message="Fill all the informations")
    else:
        try:
            with open("data.json", "r") as file:
                #reading old data
                data = json.load(file)
                # updating old data with new data

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(new_data, file, indent=4)

        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, 'end')
            entry_pw.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries

entry_website = Entry(width=32)
entry_website.grid(row=1, column=1)
entry_website.focus()

entry_username = Entry(width=50)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "kohldan@gmail.com")

entry_pw = Entry(width=32)
entry_pw.grid(row=3, column=1)

#buttons

button_generate = Button(text="Generate password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=44, command=save_text)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", width=15, command=search)
button_search.grid(row=1, column=2)

window.mainloop()
