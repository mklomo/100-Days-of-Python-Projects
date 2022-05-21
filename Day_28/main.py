import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    # Stop the time
    if timer is not None:
        window.after_cancel(timer)
    else:
        # Do Nothing
        pass
    # Reset the timer text
    canvas.itemconfig(timer_text, text="00:00")
    #reset the title label to "Timer"
    canvas.itemconfig(title_text, text="TIMER")
    #reset check marks
    text_label["text"] = ""
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    work_short_break = SHORT_BREAK_MIN * 60
    work_long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfig(title_text, text="LONG BREAK", fill=RED)
        count_down(work_long_break)
    elif reps % 2 == 0:
        canvas.itemconfig(title_text, text="SHORT BREAK", fill=PINK)
        count_down(work_short_break)
    else:
        canvas.itemconfig(title_text, text="WORK TIME")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"
        text_label["text"] = marks

# ---------------------------- UI SETUP ------------------------------- #

# Creating the window
window = Tk()
window.title("Pomodoro")
window.minsize(width=450, height=400)
window.config(padx=100, pady=25, bg=YELLOW)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# Text Label
text_label = Label(fg=GREEN, bg=YELLOW)
text_label.grid(column=1, row=3)

# Creating the Canvas
canvas = Canvas(width=200, height=280, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 150, image=tomato_img)
timer_text = canvas.create_text(100, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
title_text = canvas.create_text(100, 25, text="TIMER", fill=GREEN, font=(FONT_NAME, 25, "normal"))
canvas.grid(column=1, row=1)

# Window event listener
window.mainloop()
