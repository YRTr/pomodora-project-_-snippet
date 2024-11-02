from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLACK = "#151515"
YELLOW = "#f7f5dd"
WHITE = "#eef7ff"
WORKING = "#00ffd1"
NEUTRAL = "#86fffa"
SHORT_BREAK = "#f6f1e9"
LONG_BREAK = "#b6fffa"
FONT_NAME = "Arimo"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 'None'

# ---------------------------- TIMER RESET ------------------------------- #


def reset_b():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", background=NEUTRAL)
    check_marks.config(text="")
    window.config(bg=NEUTRAL)
    canvas.config(bg=NEUTRAL)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_b():
    global reps
    reps += 1

    minimum_worktime = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        window.config(bg=LONG_BREAK)
        title.config(text="------long-break------", background=LONG_BREAK)
        canvas.config(bg=LONG_BREAK)
        check_marks.config(background=LONG_BREAK)
    elif reps % 2 == 0:
        count_down(short_break)
        window.config(bg=SHORT_BREAK)
        title.config(text="------small-break------", background=SHORT_BREAK)
        canvas.config(bg=SHORT_BREAK)
        check_marks.config(background=SHORT_BREAK)
    else:
        count_down(minimum_worktime)
        title.config(text="WORKTIME", background=WORKING)
        window.config(bg=WORKING)
        canvas.config(bg=WORKING)
        check_marks.config(background=WORKING)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_b()
        marks=""
        mark_sessions = math.floor(reps / 2)
        for _ in range(mark_sessions):
            marks += "✔"
        check_marks.config(text='marks')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro project")
window.config(padx=150, pady=100, bg=NEUTRAL)

canvas = Canvas(width=200, height=224, bg=NEUTRAL, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=("Arial", 24, "bold"), foreground=BLACK, background=NEUTRAL)
title.grid(column=1, row=0)

start_button = Button(text="start", highlightthickness=0, command=start_b, background=WHITE, font="Calibri")
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset_b, background=WHITE, font="Calibri")
reset_button.grid(column=3, row=2)

check_marks = Label(background=NEUTRAL, foreground=RED)
check_marks.grid(column=1, row=2)

window.mainloop()
