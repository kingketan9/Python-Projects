from turtle import Turtle,Screen
screen = Screen()

class Move(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.penup()
        self.x =-230
        self.goto(0,self.x)
        self.left(90)

    def position(self):
        return self.xcor(),self.ycor()


    def move_up(self):
        self.x+=10
        self.goto(0, self.x)

    def move_down(self):
        self.x -= 10
        self.goto(0, self.x)
