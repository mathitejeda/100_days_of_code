from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
    def move(self):
        xpos = self.xcor() + self.xmove
        ypos = self.ycor() + self.ymove
        self.goto(xpos, ypos)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def point(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

