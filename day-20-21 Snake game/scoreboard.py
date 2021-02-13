from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.write(f"Game over. Final score: {self.score}",False,ALIGNMENT,FONT)

    def track_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, font=FONT)
