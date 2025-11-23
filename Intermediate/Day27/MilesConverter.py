from tkinter import *

# Conversion Function created
def converter(miles):
    km=miles*1.609344
    return round(km,3)

# Window Created
window=Tk()
window.title("Miles Converter")
window.minsize(width=200,height=200)
window.config(padx=100,pady=20)


# user Input taken
user_input=Entry(width=10)
user_input.grid(column=2,row=2)


# button Created
def button_clicked():
    miles=float(user_input.get())
    km=converter(miles)
    label.config(text=km)

button=Button(text="Convert",command=button_clicked)
button.grid(column=3,row=3)

# Output Label
label=Label(text="0")
label.grid(column=2,row=4)

# milesLabel
milabels=Label(text="Miles.",font=("Arial",8,"bold"))
milabels.grid(column=3, row=2)

# Kilometers lable
kilolables=Label(text="Km.",font=("Arial",8,"bold"))
kilolables.grid(column=3, row=4)

# Heading craeted
heading=Label(text="Miles to Kilometer Converter",font=("Courrier",12,"bold"))
heading.grid(column=2, row=1)

window.mainloop()