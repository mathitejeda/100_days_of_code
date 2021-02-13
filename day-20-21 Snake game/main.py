from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Food Colition
    if snake.snake_head.distance(food) < 15:
        print("nomini")
        scoreboard.track_score()
        snake.extend()
        food.refresh()
#Wall colition
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.game_over()
        game_on = False
#Snake collition
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
