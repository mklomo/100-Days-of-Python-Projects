
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # Specifying data type expected from the input
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        # Set the size of the window
        self.window.minsize(width=600, height=800)
        self.window.maxsize(width=600, height=800)
        self.window.config(bg=THEME_COLOR)
        self.canvas = Canvas(width=500, height=500, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50)
        self.canvas_starter_text = self.canvas.create_text((250, 250), text="Welcome to the Marvin's Quizzler", font=("Arial", 30, "italic"), width=460)
        self.score = 0
        self.score_text = Label(text=f"Score: {self.score}", font=("Tahoma", 20, "normal"), bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1, pady=20)
        # Specify the button
        self.true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.true_image, bd=0, highlightthickness=0, command=self.true_pressed)
        # Specify the position
        self.right_button.grid(row=2, column=0, pady=50)
        # Specify the button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, bd=0, highlightthickness=0, command=self.false_pressed)
        # Specify the position
        self.wrong_button.grid(row=2, column=1, pady=50)
        self.get_next_question()
        self.new_game = Button(text="Replay", bd=0, highlightthickness=0, bg="red", command=self.play_again, font=("Tahoma", 20, "normal"))
        # Specify the position
        self.new_game.grid(row=0, column=0, pady=50)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_starter_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_starter_text, text="You have reached the end of the question!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def play_again(self):
        self.quiz.replay()
        self.score_text.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_starter_text, text=q_text)





