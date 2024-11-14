from tkinter import *
from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizzInterface:
        def __init__(self, quiz_brain: QuizBrain):
            self.quiz_brain = quiz_brain
            self.window = Tk()
            self.window.title("Quizzler")
            self.window.config(padx=20, pady=20, bg=THEME_COLOR)
            self.score_label = Label(text=f"Score: {self.quiz_brain.score}",fg="white", bg=THEME_COLOR, font=FONT)
            self.score_label.grid(column=1, row=0)
            self.canvas = Canvas(width=300, height=250, bg="white")
            self.canvas_text = self.canvas.create_text(150, 125, text="Question", width=280, font=FONT, fill=THEME_COLOR)
            self.canvas.grid(column=0, row=1, columnspan=2, pady= 50)

            true_image = PhotoImage(file="images/true.png")
            self.true_button = Button(image=true_image, width=100, height=100, highlightthickness=0
                                      , bg=THEME_COLOR, border=False, command=self.true_pressed)
            self.true_button.grid(column=0, row=2)

            false_image = PhotoImage(file="images/false.png")
            self.false_button = Button(image=false_image, width=100, height=100, highlightthickness=0,
                                       bg=THEME_COLOR, border=False, command=self.false_pressed)
            self.false_button.grid(column=1, row=2)

            self.get_next_question()
            self.window.mainloop()

        def get_next_question(self):
            self.canvas.config(bg="white")
            if self.quiz_brain.still_has_questions():
                next_question = self.quiz_brain.next_question()
                self.canvas.itemconfig(self.canvas_text, text=next_question)
            else:
                self.canvas.itemconfig(self.canvas_text, text="You've reach the end of the quiz.")
                self.false_button.config(state="disabled")
                self.true_button.config(state="disabled")
        def true_pressed(self):
            is_right = self.quiz_brain.check_answer("True")
            self.give_feedback(is_right)

        def false_pressed(self):
            is_right = self.quiz_brain.check_answer("False")
            self.give_feedback(is_right)

        def give_feedback(self, is_right: bool):
            if is_right:
                self.canvas.config(bg="green")
                self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            else:
                self.canvas.config(bg="red")

            self.window.after(1000, self.get_next_question)