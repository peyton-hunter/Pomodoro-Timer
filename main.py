from tkinter import *
import math

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


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer")
    check_tracking.config(text='')
    global reps
    reps = 0


def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        heading.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        heading.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        heading.config(text="Work", fg=GREEN)


def countdown(count):

    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        checks = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            checks += "✔"
        check_tracking.config(text=checks)


window = Tk()
window.title("Pomodoro Study Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, '35', 'bold'))
canvas.grid(row=1, column=1)

heading = Label(text="Timer", font=(FONT_NAME, '45', 'bold'), bg=YELLOW, fg=GREEN)
heading.grid(row=0, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start)
start_button.grid(row=2, column=0)

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(row=2, column=2)

check_tracking = Label(fg=GREEN, bg=YELLOW)
check_tracking.grid(row=3, column=1)

window.mainloop()
