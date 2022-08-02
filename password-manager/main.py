# import email
from email import message
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for char in range(randint(8, 10))]
  password_symbols = [choice(symbols) for char in range(randint(2, 4))]
  password_numbers = [choice(numbers) for char in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)
  password_input.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- MANAGE PASSWORD ------------------------------- #

def save():
  website = website_input.get()
  password = password_input.get()
  username = username_input.get()
  new_data = {
    website: {
      "username": username,
      "password": password,
    }
  }

  if len(password) == 0 or len(website) == 0:
    messagebox.showerror(title="Error", message="Please enter all required information.")
  else:  
      try:
        with open("password_data.json", "r") as password_file: 
          data = json.load(password_file)
          
      except FileNotFoundError:
        with open("password_data.json", "w") as password_file:
          json.dump(new_data, password_file, indent=4)

      else:
        data.update(new_data)

        with open("password_data.json", "w") as password_file:
          json.dump(data, password_file, indent=4)

      finally:  
        website_input.delete(0, END)
        password_input.delete(0, END)
    
def find_password():
  website = website_input.get()
  try:
    with open("password_data.json") as password_file:
        data = json.load(password_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No data file found")
  
  else:
    if website in data:
      username = data[website]["username"]
      password = data[website]["password"]
      messagebox.showinfo(title=website, message=f"Email: {username}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
  

  
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)
website_input = Entry(width=22)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:", font=("Arial", 10))
username_label.grid(column=0, row=2)
username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(END, "shout.citlali@gmail.com")

password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)
password_input = Entry(width=22)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()