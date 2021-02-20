from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#fb743e"
BLUE = "#383e56"
GREEN = "#9fb8ad"
LIGHTER_GREEN = "#c5d7bd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(actual_timer,text = "00:00")
    checkmark.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="take a long break", fg=ORANGE)
    if reps % 2 != 0:
        count_down(work_sec)
        timer_text.config(text="work time", fg=BLUE)
    else:
        count_down(short_break_sec)
        timer_text.config(text="take a short break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(actual_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark.config(text="✔" * (reps - 1))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LIGHTER_GREEN)
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=LIGHTER_GREEN, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
actual_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Labels
timer_text = Label(text="Pomodoro clock", fg=BLUE, bg=LIGHTER_GREEN, font=(FONT_NAME, 24, "bold"))
timer_text.grid(row=0, column=1)

checkmark = Label(bg=LIGHTER_GREEN)
checkmark.grid(row=3, column=1)
# Buttons

start_button = Button(text="start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset",command = reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
