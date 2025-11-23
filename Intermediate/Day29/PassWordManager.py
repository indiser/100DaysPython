from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generate_password():
    passWord=[]
    
    passWord_letter=[random.choice(letters) for _ in range(8)]
    passWord_symbol=[random.choice(symbols) for _ in range(2,6)]
    passWord_numbers=[random.choice(numbers) for _ in range(3,6)]
    passWord=passWord_letter+passWord_symbol+passWord_numbers
    random.shuffle(passWord)
    passWord="".join(passWord)

    passWordText_entry.delete(0,END)
    passWordText_entry.insert(0,passWord)
    pyperclip.copy(passWord)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website=web_entry.get().title()
    email=email_entry.get()
    password=passWordText_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day29/saved_password.txt", "a") as filp:
                filp.write(f"Website:{website} | Email:{email} | Pasword:{password}")
            with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day29/saved_password.json", "r") as filp:
                data=json.load(filp)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day29/saved_password.json", "w") as filp:
                json.dump(new_data, filp, indent=4)
        else:
            data.update(new_data)
            with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day29/saved_password.json", "w") as filp:
                json.dump(data, filp, indent=4)
        finally:
            web_entry.delete(0,END)
            passWordText_entry.delete(0,END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website=web_entry.get().title()
    try:
        with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day29/saved_password.json", "r") as filp:
            data=json.load(filp)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Non Existance", message="The website doesnt exit in the database")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("PassWord Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
lock=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day29/logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(row=0,column=1)


# Website label
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

# website Entry
web_entry=Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()

# Email Label
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

# Email Entry
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"admin@google.com")

# password label
passWord_label=Label(text="Password:")
passWord_label.grid(row=3,column=0)

# pass_entry
passWordText_entry=Entry(width=21)
passWordText_entry.grid(row=3,column=1)

# Generate passWord Button
generate_passWord=Button(text="Generate PassWord",command=generate_password)
generate_passWord.grid(row=3,column=2)

# Add Button
add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

# Search Button
search_button=Button(text="Search",width=8,command=search_website)
search_button.grid(row=1, column=3)

window.mainloop()