import turtle as t

def move_forward():
    turture.forward(10)
def move_back():
    turture.backward(10)
def move_right():
    turture.right(10)
def move_left():
    turture.left(10)

def clear_screen():
    turture.clear()
    turture.penup()
    turture.home()
    

turture=t.Turtle()
screen=t.Screen()



screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()