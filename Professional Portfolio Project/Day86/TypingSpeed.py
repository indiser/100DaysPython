from tkinter import *
from timeit import default_timer as timer
import random
from faker import Faker

fake=Faker()
len=20

words = fake.words(nb=len)

def go_to_entry():
    entry_word.focus_set()

def start_exam():
    global start_time,word_type
    word_type=random.choice(words)
    label_word.config(text=word_type)
    entry_word.delete(0,END)
    start_time=timer()
    go_to_entry()

def check_result(event):
    end_time=timer()
    typed_word=entry_word.get()

    if typed_word==word_type:
        result_label.config(text=f"Correct! Time: {end_time - start_time:.2f} seconds")
    else:
        result_label.config(text="Incorrect! Try again.")
        entry_word.delete(0,END)
        go_to_entry()


window=Tk()

window.title("Typing Speed Test")
window.geometry("600x300")

instructions=Label(window,text="Type the word shown below:", font=("arial",14))
instructions.pack(pady=10)

label_word=Label(window,text="",font=("arial",14),fg="blue")
label_word.pack(pady=10)

Tell_label=Label(window,text="Press 'Enter' to check your time", font=("arial",10))
Tell_label.pack(pady=10)

entry_word = Entry(window, font=("arial", 14))
entry_word.pack(pady=10)

entry_word.bind("<Return>",check_result)

start_button=Button(window,text="Start",command=start_exam,bg="green", fg="white", font=("arial", 12))
start_button.pack(pady=10)

result_label = Label(window, text="", font=("Arial", 14), fg="red")
result_label.pack(pady=10)

window.mainloop()