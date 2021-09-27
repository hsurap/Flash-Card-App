BACKGROUND_COLOR = "#B1DDC6"

import  tkinter
import pandas
import random


word={}

try:
    data=pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    word=original_data.to_dict(orient="records")
else:
    data = data.to_dict(orient="records")

# print(data)


def is_known():
    data.remove(word)
    new_data=pandas.DataFrame(data)
    new_data.to_csv("data/word_to_learn.csv",index=False)
    next_word()

def english_word():
    # print("hello")

    canvas.itemconfig(canvas_image,image=back_img)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word,text=word["English"],fill="white")



def next_word():
    global word,timer
    window.after_cancel(timer)
    word=random.choice(data)
    # print(word)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=word["French"],fill="black")
    canvas.itemconfig(canvas_image,image=front_img)
    window.after(3000, english_word)

window=tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer=window.after(3000,english_word)

canvas = tkinter.Canvas( width = 800, height = 526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
front_img = tkinter.PhotoImage(file="./images/card_front.png")
back_img=tkinter.PhotoImage(file="./images/card_back.png")
canvas_image=canvas.create_image(400,263, image=front_img)
card_title=canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button=tkinter.Button(image=wrong_image,command=next_word)
wrong_button.config(highlightthickness=0)
wrong_button.grid(row=1,column=0)

right_image = tkinter.PhotoImage(file="./images/right.png")
right_button=tkinter.Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_word()

window.mainloop()