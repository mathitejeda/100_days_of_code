from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_segment()
        self.snake_head = self.segments[0]
    def create_segment(self):
        for position in STARTING_POS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_xpos = self.segments[segment_number - 1].xcor()
            new_ypos = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_xpos, new_ypos)
        self.snake_head.forward(MOVE_DISTANCE)
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)