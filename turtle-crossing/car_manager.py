from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            new_car.goto(x=300, y=y_pos)
            new_car.speed(self.move_speed)
            self.cars.append(new_car)
        else:
            pass

    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def go_zoom(self):
        self.move_speed += MOVE_INCREMENT
