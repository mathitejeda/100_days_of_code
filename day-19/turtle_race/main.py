from turtle import Turtle, Screen
import  random

screen = Screen()

screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
is_race_on = False
colors = ["red", "yellow", "blue", "green", "pink", "purple", "orange"]
y_positions = [180,143,86,29,-28,-85,-142]
turtles = []
winning_color = ""
def create_turtle(color, xpos,ypos):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=xpos,y=ypos)
    return  turtle

for i in range (6):
    tortuga = create_turtle(colors[i],-230,y_positions[i])
    turtles.append(tortuga)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

if bet == winning_color:
    print(f"You won! {winning_color} wins the race!")
else:
    print(f"You loose, {winning_color} won the race")

screen.exitonclick()
