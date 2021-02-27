from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
to_learn = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")


# -------------------- Functions ------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def update_file():
    to_learn.remove(current_card)
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------- UI Setup -------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
# Load images

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right_check = PhotoImage(file="images/right.png")
wrong_check = PhotoImage(file="images/wrong.png")

# Canvas work

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_check, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_check, bg=BACKGROUND_COLOR, highlightthickness=0, command=update_file)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
