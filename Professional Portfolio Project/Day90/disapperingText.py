from tkinter import *
from tkinter.messagebox import showinfo,showerror
import ttkbootstrap as ttk
import os

script_dir=os.path.dirname(os.path.abspath(__file__))

user_input=""
timer=None

def start_calculation(event):
    global timer,user_input

    if timer is not None:
        window.after_cancel(timer)
    
    if event.keysym=="BackSpace":
        user_input=user_input[0: len(user_input)-1]
    elif event.char:
        user_input+=event.char
    
    timer=window.after(10000,reset_timer)

    return

def reset_timer():
    global timer,user_input
    textField.delete('1.0',END)
    user_input=""
    timer=None
    return

def save_input():
    global timer,user_input

    if user_input == "":
        return
    
    file_name=f"{user_input[:5]}.txt"
    
    try:
        with open(os.path.join(script_dir,file_name),"w") as filp:
            filp.write(user_input)

        showinfo("Saved",f"Saved as {file_name}")
    except Exception as e:
        showerror("Error",f"Could not be saved..{e}")
    finally:
        if timer is not None:
            window.after_cancel(timer)
            timer=None
        
        reset_timer()
        return



HEADING="WRITE WITH DISAPPERING INK."
INSTRUCTIONS="Text will diapper if idle for 10 seconds...."

window=ttk.Window(themename="superhero")

window.title("Disappering Text Editor")
window.minsize(height=500,width=500)

heading=ttk.Label(text=HEADING)
heading.grid(column=0,row=0,padx=50,pady=50)

instructions=ttk.Label(text=INSTRUCTIONS)
instructions.grid(column=0,row=1,padx=20,pady=20)

textField=ttk.Text(window,height=10,width=60,cursor="xterm")
textField.grid(column=0,row=2,padx=20,pady=20)
textField.bind("<KeyPress>",start_calculation)

save_btn=ttk.Button(text="Save",command=save_input)
save_btn.grid(column=0,row=3,padx=20,pady=20,sticky="ew")

window.grid_rowconfigure(2, weight=1)
window.mainloop()