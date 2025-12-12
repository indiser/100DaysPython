from tkinter import *
from data import question_data
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain


        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.scoreBoard=Label(text=f"Score: {0}")
        self.scoreBoard.config(padx=20,pady=20,bg=THEME_COLOR,fg="white")
        self.scoreBoard.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250)
        self.canvas.config(bg="white")
        self.question_text=self.canvas.create_text(150,125,text="PlaceHolder",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.right_button_image=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day34/images/true.png")
        self.wrong_button_image=PhotoImage(file="C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day34/images/false.png")
        
        self.correctButton=Button(image=self.right_button_image,width=100,height=97,highlightthickness=0,command=self.right_button)
        self.correctButton.config(bg=THEME_COLOR)
        self.correctButton.grid(row=2,column=0)

        self.wrongButton=Button(image=self.wrong_button_image,width=100,height=97,highlightthickness=0,command=self.false_button)
        self.wrongButton.config(bg=THEME_COLOR)
        self.wrongButton.grid(row=2,column=1)

        self.get_questions()

        self.window.mainloop()



    def get_questions(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreBoard.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correctButton.config(state="disabled")
            self.wrongButton.config(state="disabled")

    def right_button(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)



    def false_button(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_questions)