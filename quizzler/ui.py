from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", font=("arial", 20, "italic"),
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg = "white")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text,text = " You're still here? It's Over. Go Home. Go.",width = 280)
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def true_pressed(self):
        result = self.quiz.check_answer("true")
        self.feedback(result)

    def false_pressed(self):
        result = self.quiz.check_answer("false")
        self.feedback(result)

    def feedback(self, result):
        if result:
            self.canvas.config(bg = "green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.get_next_question)
