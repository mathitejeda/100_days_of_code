from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)

    def move_fw(self):
        if self.heading() != UP:
            self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_bw(self):
        if self.heading() != DOWN:
            self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.heading() != LEFT:
            self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.heading() != RIGHT:
            self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)
