from operator import index
from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    global current_card
    card_canvas.itemconfig(language_text, text="English", fill="white")
    card_canvas.itemconfig(word_text, text=current_card["English"].title(), fill="white")
    card_canvas.itemconfig(card_image, image=card_back_image)

def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(language_text, text="French", fill="black")
    card_canvas.itemconfig(word_text, text=current_card["French"].title(), fill="black")
    card_canvas.itemconfig(card_image, image=card_front_image)

    flip_timer = window.after(3000, flip_card)

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png", width=800, height=526)
card_back_image = PhotoImage(file="images/card_back.png", width=800, height=526)
card_image = card_canvas.create_image(400, 263, image=card_front_image)
language_text = card_canvas.create_text(400, 150, text=f"", font=LANGUAGE_FONT)
word_text = card_canvas.create_text(400, 263, text=f"", font=WORD_FONT)
card_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, width=100, height=100, highlightthickness=0, border=False, command=next_card)
wrong_button.grid(column=0,row=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, width=100, height=100, highlightthickness=0, border=False, command=is_known)
right_button.grid(column=1,row=2)

next_card()

window.mainloop()