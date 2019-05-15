
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import os
import socket

root = Tk()
root.title('Hasil Voting')
root.geometry('700x300')

LabelOP = Label(root,text = "Perolehan Voting ")
LabelOP.grid(row = 1,column = 2)
LabelOP.config(font=("Courier", 14))
LabelOP = Label(root,text = "One Piece   : ")
LabelOP.grid(row = 2,column = 1)
LabelOP.config(font=("Courier", 14))
LabelOP = Label(root,text = "Bleach      : ")
LabelOP.grid(row = 3,column = 1)
LabelOP.config(font=("Courier", 14))
LabelOP = Label(root,text = "Fairy Tail  : ")
LabelOP.grid(row = 4,column = 1)
LabelOP.config(font=("Courier", 14))
LabelOP = Label(root,text = "Naruto      : ")
LabelOP.grid(row = 5,column = 1)
LabelOP.config(font=("Courier", 14))
LabelOP = Label(root,text = "Dragon Ball : ")
LabelOP.grid(row = 6,column = 1)
LabelOP.config(font=("Courier", 14))


root.mainloop()