from turtle import Turtle
from data import colors
import turtle
import random


turtle.colormode(255)
b =[]
class Car (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(1,3)
        self.goto(350, random.randint(-250, 250))
        self.setheading(180)
        self.color(random.choice(colors))
        self.shape("square")
        rand = random.randint(1,10)
        if rand ==2:
            b.append(self.clone())
        self.hideturtle()

    def move(self):
         l = len(b)
         for i in range(0,l):
                    b[i].forward(20)

    def collision(self,Y):
                for car in b:
                          if car.distance(Y)<40:
                                     val = False
                                     return val
