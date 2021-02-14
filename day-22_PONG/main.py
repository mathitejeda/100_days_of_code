from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

game_on = True

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect top bottom collision
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9


    # Rpaddle miss
    if ball.xcor() >= 390:
        ball.point()
        score.l_point()

    # Lpaddle miss
    if ball.xcor() <= -390:
        ball.point()
        score.r_point()
screen.exitonclick()
