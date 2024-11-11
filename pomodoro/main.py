
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_brake_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count_number):
    global reps
    global timer

    minutes = count_number // 60
    seconds = count_number % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count_number > 0:
        timer = window.after(1000, count_down, count_number - 1)
    else:
        count = reps // 2
        check_marks = ""
        for _ in range(count):
            check_marks += "✔"
        check_mark.config(text=check_marks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(width=500, height=500, bg=YELLOW)
window.title("Pomodoro app")
window.config(padx=100,pady=50)
tomato_img = PhotoImage(file="tomato.png")
window.iconphoto(True, tomato_img)
#Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness = 0, justify="right")
timer_label.grid(column = 1, row = 0)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column = 1, row = 3)

#Canvas
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", justify="center", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

#Buttons
start_button = Button(text="Start", command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column = 2, row = 2)

window.mainloop()