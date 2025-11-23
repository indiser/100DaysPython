from tkinter import *

window=Tk()
window.title("GUI")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)


label=Label(text="Label",font=("Arial",24,"bold"))
# label.pack()
label.grid(column=0,row=0)

# def button_clicked():
#     label.config(text="Button got clicked")


input=Entry(width=10)
input.grid(column=3, row=2)

def button_clicked():
    string=input.get()
    label.config(text=string)

button=Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)

new_button=Button(text="New Button")
new_button.grid(column=2,row=0)

window.mainloop()