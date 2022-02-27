from turtle import Screen,Turtle
from move import Move
from cars import Car
import time

move = Move()
screen = Screen()
tut =Turtle()



screen.screensize(canvwidth=500,canvheight=500)
screen.bgcolor("violet")

game = True
screen.tracer(0)
screen.listen()
screen.onkeypress(move.move_up, "Up")
screen.onkeypress(move.move_down, "Down")

speed = 0.1
level=0
while game==True:
        car = Car()
        tut.penup()
        tut.goto(0,250)
        tut.write(f"Level = {level}",move=False, align="center", font=("Arial", 20, "bold"))
        tut.clear()
        time.sleep(speed)
        screen.update()
        car.move()
        Y = move.position()
        check = car.collision(Y)
        if(check==False):
            tut.goto(0,0)
            game=False
            tut.write("GAME OVER",move=False, align="center", font=("Arial", 20, "bold"))
            tut.goto(0, 250)
            tut.write(f"Level = {level}", move=False, align="center", font=("Arial", 20, "bold"))
        tut.hideturtle()
        if move.distance(0,230)<20:
                move.x=-230
                speed = speed-0.01
                level+=1












screen.exitonclick()
