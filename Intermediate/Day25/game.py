import pandas as pd
import turtle

screen=turtle.Screen()
screen.title("U.S state Guessing game")
image="india_states_blank.gif"
screen.addshape(image)
screen.setup(width=511, height=600)
turtle.shape(image)

data=pd.read_csv("india_optimized.csv")
state_list=data["state"].to_list()
guessed_states=[]

while len(guessed_states) < 36:
    user_input=screen.textinput(title=f"{len(guessed_states)}/36 states correct", prompt="What is the state??")
    if user_input==None:
        break
    user_input=user_input.title()
    if user_input in state_list and user_input not in guessed_states:
        guessed_states.append(user_input)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==user_input]
        t.goto(int(state_data["x"]),int(state_data["y"]))
        t.write(user_input, align="center", font=("Arial", 6, "bold"))

t=turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0,0)
if len(guessed_states)==36:
    t.write("You Won!!", align="center", font=("Arial", 30, "normal"))
else:
    t.write("You Lose!!", align="center", font=("Arial", 30, "normal"))


missed_states_list=[state for state in state_list if state not in guessed_states]
missed_states_data=data[data["state"].isin(missed_states_list)]
missed_states_data.to_csv("missed_states.csv")

screen.exitonclick()


