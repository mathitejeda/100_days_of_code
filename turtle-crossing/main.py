import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
game_is_on = True
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_fw, "Up")
screen.onkey(player.move_bw, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == 280:
        player.start()
        car_manager.go_zoom()
        scoreboard.level_up()
screen.exitonclick()
