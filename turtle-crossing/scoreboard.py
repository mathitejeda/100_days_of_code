from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-221,250)
        self.hideturtle()
        self.write_level()
    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}",0, "center", FONT)
    def level_up(self):
       self.level+=1
       self.write_level()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game over.",0,"center",FONT)

