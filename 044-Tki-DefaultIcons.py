#!/usr/bin/env python

# https://www.tutorialspoint.com/python/tk_bitmaps.htm

from Tkinter import *
import Tkinter

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="error", relief=RAISED,\
                         bitmap="error")
B2 = Tkinter.Button(top, text ="hourglass", relief=RAISED,\
                         bitmap="hourglass")
B3 = Tkinter.Button(top, text ="info", relief=RAISED,\
                         bitmap="info")
B4 = Tkinter.Button(top, text ="question", relief=RAISED,\
                         bitmap="question")
B5 = Tkinter.Button(top, text ="warning", relief=RAISED,\
                         bitmap="warning")
B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
