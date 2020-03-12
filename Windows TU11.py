lst = []

for i in range (3):
    names = input("name?")
    lst.append(names)
    print(lst)

import tkinter
import random

window = tkinter.Tk()

def RandomNumber():
    MyRandom = random.choice(lst)
    name.configure(text="Name: " + str(MyRandom))

MyTitle = tkinter.Label(window, text="Random Name Generator",font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="OK", command=RandomNumber)
MyButton.pack()

name = tkinter.Label(window, font="Helvetica 16 bold")
name.pack()

window.mainloop()
