from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "white"
Q_TEXT_FONT = ("ariel", 20, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config( bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz_brain.score}", fg=WHITE, pady=20, padx=20, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 100, width=280, text=quiz.next_question(), fill="black", font=Q_TEXT_FONT, anchor="c")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)

        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            q_text = f"You have completed the quiz. \nYour score is {self.quiz_brain.score}"
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        is_true = self.quiz_brain.check_answer("true")
        self.give_feedback(is_true)

    def false_pressed(self):
        is_true = self.quiz_brain.check_answer("false")
        self.give_feedback(is_true)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

