BACKGROUND_COLOR = "#B1DDC6"
FLIP_DELAY = 3000

from tkinter import *
import pandas as pd
import random



# create New Flash cards
data=pd.read_csv("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day31/data/french_words.csv")
new_dict={row["French"]:row["English"] for (index,row) in data.iterrows()}
key=random.choice(list(new_dict.keys()))


# Flip the cards
def flip():
    # Back Card
    front_card_canvas.itemconfig(card_image,image=card_back_image)
    front_card_canvas.itemconfig(card_text,text="English",fill="white")
    front_card_canvas.itemconfig(card_ans,text=f"{new_dict[key]}",fill="white")

#Right
def correct_click():
    global key
    global timer
    window.after_cancel(timer)
    with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day31/progress.txt","a") as filp:
        filp.write(f"{key},{new_dict[key]}\n")
    new_dict.pop(key)
    cross_click()




# Cross
def cross_click():
    global key
    global timer
    window.after_cancel(timer)
    if len(new_dict) == 0:
        front_card_canvas.itemconfig(card_image, image=card_front_image)
        front_card_canvas.itemconfig(card_text, text="Completed!", fill="black")
        front_card_canvas.itemconfig(card_ans, text="All words learned!", fill="black")
        right_button.config(state="disabled")  # Add this
        wrong_button.config(state="disabled")  # Add this
        return
    key=random.choice(list(new_dict.keys()))
    front_card_canvas.itemconfig(card_image, image=card_front_image)
    front_card_canvas.itemconfig(card_text, text="French",fill="black")
    front_card_canvas.itemconfig(card_ans, text=f"{key}", fill="black")
    timer=window.after(FLIP_DELAY,flip)




# Create the ui
window=Tk()
window.title("FlashCard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_front_image=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day31/images/card_front.png")
card_back_image=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day31/images/card_back.png")
right_image=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day31/images/right.png")
wrong_image=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day31/images/wrong.png")

# Front Card
front_card_canvas=Canvas(width=800,height=526)
card_image=front_card_canvas.create_image(400,263,image=card_front_image)
front_card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_text=front_card_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_ans=front_card_canvas.create_text(400, 263, text=f"{key}", font=("Ariel", 60, "bold"))
front_card_canvas.grid(row=0,column=0,columnspan=2)



# Right
right_button=Button(image=right_image,highlightthickness=0,command=correct_click)
right_button.config(bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

# Wrong
wrong_button=Button(image=wrong_image,highlightthickness=0,command=cross_click)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)



timer=window.after(FLIP_DELAY,flip)



window.mainloop()