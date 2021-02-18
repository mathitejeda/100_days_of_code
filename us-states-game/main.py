import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_boe = turtle.Turtle()
states_boe.penup()
states_boe.hideturtle()

guessed_states = []

states_data = pandas.read_csv("50_states.csv")
states_names = states_data.state.to_list()
while len(guessed_states) != 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 guessed", prompt="Guess all the states and win nothing!")
    answer = answer.title()
    if answer == "Exit":
        states_to_learn = [state for state in states_names if state not in guessed_states]
        break
    if answer in states_names:
        xpos = int(states_data[states_data.state == answer].x)
        ypos = int(states_data[states_data.state == answer].y)
        states_boe.goto(xpos, ypos)
        states_boe.write(answer)
        guessed_states.append(answer)

learn_data = pandas.DataFrame(states_to_learn)
learn_data.to_csv("states_to_learn.csv")