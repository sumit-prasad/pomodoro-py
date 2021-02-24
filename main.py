# !/usr/bin/ python3

from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK_WORK = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Reset the timer
    :return:
    """
    # Returns true if user clicks yes on dialog box
    choice = messagebox.askyesno("Confirm Reset", "Do you want to reset the timer?")

    if choice:
        global TIMER, REPS
        # Global variables and local variable reset
        REPS = 0
        window.after_cancel(TIMER)
        check_label.config(text="")
        canvas.itemconfig(timer_text, text=f"00:00")
        time_label.config(text="Timer")
        start_button["state"] = "normal"


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Start the timer
    :return:
    """
    global REPS
    # For each timer increment reps by 1
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="L-Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="S-Break", fg=PINK)
    elif REPS % 2 != 0:
        count_down(work_sec)
        time_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global CHECK_WORK
    start_button["state"] = "disabled"
    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    if count_minute < 10:
        count_minute = f"0{count_minute}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        window.focus_force()
        start_timer()
        if REPS % 2 == 0:
            CHECK_WORK += 1
            check_label.config(text="✓" * CHECK_WORK)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

# Timer label
time_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=GREEN)
time_label.grid(row=1, column=2)

# Canvas for tomato image
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_image)
timer_text = canvas.create_text(101, 140, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=2, column=2)

# Start button
start_button = Button(text="Start", highlightthickness=0, borderwidth=0, command=start_timer)
start_button.grid(row=3, column=1)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.grid(row=3, column=3)

# Check mark label
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_label.grid(row=4, column=2)


window.mainloop()
