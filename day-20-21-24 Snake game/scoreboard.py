from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_hscore()
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_hscore(self.high_score)
        self.score = 0

    def read_hscore(self):
        high_score = 0
        with open("data.txt") as data:
            high_score = data.read()
            high_score = int(high_score)
        return  high_score

    def write_hscore(self,new_hs):
        with open("data.txt",mode="w") as data:
            data.write(str(new_hs))