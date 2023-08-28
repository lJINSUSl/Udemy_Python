from tkinter import *
from tkinter import messagebox

import pandas as pd
from dataframe import Dict
import random


BACKGROUND_COLOR = "#B1DDC6"

#---------------------------Word Choice Function-----------------------




dictionary = Dict()
try:
    word_dictionary = dictionary.change('words_to_learn.xlsx')
except FileNotFoundError:
    word_dictionary = dictionary.change('word.xlsx')

# ---------------------------Import excel--------------------------------
def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dictionary)
    canvas.itemconfig(canvas_img, image = white_back)
    canvas.itemconfig(card_title,text = "English",fill = 'black')
    canvas.itemconfig(card_word,text = current_card['english'],fill = 'black')
    flip_timer = window.after(3000, show_ans)

def is_known():
    word_dictionary.remove(current_card)
    data = pd.DataFrame(word_dictionary)
    data.to_excel("words_to_learn.xlsx",index=False)
    next_card()

def show_ans():
    canvas.itemconfig(canvas_img, image=green_back)
    canvas.itemconfig(card_title, text="Korean",fill = 'white')
    canvas.itemconfig(card_word, text=f"{current_card['korean']}",fill = 'white')
# ----------------------------Code line---------------------------------

window = Tk()
window.title("Word game")
window.config(width=800,height=800,pady=50,padx=50,bg=BACKGROUND_COLOR,highlightthickness=0)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

green_back = PhotoImage(file='images/card_back.png')

flip_timer = window.after(3000,show_ans)




white_back = PhotoImage(file='images/card_front.png')
canvas_img = canvas.create_image(400,263,image = white_back)
card_title = canvas.create_text(400,150,text="English",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)






image_right = PhotoImage(file="images/right.png")
button_right = Button(image = image_right, highlightthickness=0,command=is_known)
button_right.grid(row=1,column=1)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image = image_wrong, highlightthickness=0,command=next_card)
button_wrong.grid(row=1,column=0)


next_card()






window.mainloop()