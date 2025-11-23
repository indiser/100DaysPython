from turtle import Turtle, Screen
from turture import Turture
from cars import Car
from scoreboard import Scoreboard
import time
import random

screen=Screen()
screen.setup(width=600,height=600)
screen.title("Turtle Road Crossing")
screen.listen()
screen.tracer(0)


turture=Turture()
scoreboard=Scoreboard()
cars=[]
car_speed=5


screen.onkey(turture.go_forward,"Up")
screen.onkey(turture.go_backwrd,"Down")
screen.onkey(turture.go_left,"Left")
screen.onkey(turture.go_right,"Right")


game_is_on=True
loop_count=0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    loop_count+=1
    
    if loop_count%6==0:
        new_car=Car()
        new_car.goto(300,random.randint(-250,250))
        cars.append(new_car)
    
    for car in cars:
        car.backward(car_speed)
        if car.xcor()<-320:
            car.hideturtle()
            cars.remove(car)
    
    for car in cars:
        if turture.distance(car)<20:
            game_is_on=False
            scoreboard.game_over()
    
    if turture.ycor()>280:
        turture.goto(0,-280)
        car_speed+=2
        scoreboard.level_up()


screen.exitonclick()