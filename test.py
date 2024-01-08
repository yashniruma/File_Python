#  ->  Solutinon of Type Error  :- require 1 argument self is missing ()
from tkinter import *
# import tkinter

win =Tk()
win.geometry("400x234")

class test:

    def de(self):
        print("okokokkokok")

t= test()
bt = Button(win, text="data", command=t.de)
bt.pack()

win.mainloop()
