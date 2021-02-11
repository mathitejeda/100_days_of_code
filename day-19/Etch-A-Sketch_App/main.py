from turtle import Turtle, Screen

rafa = Turtle()
screen = Screen()
rafa.shape("turtle")
rafa.color("pink")
rafa.pensize(10)


def forwards():
    rafa.forward(10)


def backwards():
    rafa.back(10)


def counter_clockwise():
    rafa.left(10)


def clockwise():
    rafa.right(10)


def clear_screen():
    rafa.clear()
    rafa.penup()
    rafa.home()


screen.listen()
screen.onkey(forwards, "Up")
screen.onkey(backwards, "Down")
screen.onkey(counter_clockwise, "Left")
screen.onkey(clockwise, "Right")
screen.onkey(clear_screen, "c")
screen.exitonclick()
