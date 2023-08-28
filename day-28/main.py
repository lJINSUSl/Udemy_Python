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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer",fg=GREEN)
    label_check.config(text="")
    canvas.itemconfig(timer_text,text = "00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 1:
        label_timer.config(text="Work", fg=GREEN)
        count_down(2)

    elif reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(3)

    else:
        label_timer.config(text="Break", fg=PINK)
        count_down(1)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        label_check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

import tkinter


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label_timer = tkinter.Label(text="Timer",font= (FONT_NAME,35,"bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0,column=1)



label_check = tkinter.Label(text="", bg=YELLOW, fg=GREEN)
label_check.grid(row=3,column=1)


canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file = 'tomato.png')
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white", font = (FONT_NAME, 35,"bold"))
canvas.grid(row=1,column=1)

button_start = tkinter.Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)
button_Reset = tkinter.Button(text="Reset", command=reset_timer)
button_Reset.grid(row=2, column=2)




window.mainloop()