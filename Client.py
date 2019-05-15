from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import os
import socket

pesan = ""
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(("192.168.1.14",8000))


def SimpanVoting():
    if(v.get() == 2):
        pesan = "onepiece"
    elif(v.get == 1):
        pesan = "bleach"
    elif(v.get() == 3):
        pesan = "naruto"
    elif(v.get() == 4):
        pesan = "dragonball"
    elif(v.get() == 5):
        pesan = "fairytail"
    else:
        print("Anda Belum Memilih")
    socket.send(str.encode(pesan))
    socket.close()
    

root = Tk()
root.title('Voting Anime')
root.geometry('1100x600')
v = tk.IntVar()

theLabel = Label (root, text="Voting Anime Favoritmu")
theLabel.grid(row = 0,column = 3)
theLabel.config(font=("Courier", 24))

imgBleach = Image.open("bleach.jpg")
imgBleach = imgBleach.resize((150, 150), Image.ANTIALIAS)

imgDragonBall = Image.open("dragonBall.jpg")
imgDragonBall = imgDragonBall.resize((150, 150), Image.ANTIALIAS)

imgNaruto = Image.open("naruto.jpg")
imgNaruto = imgNaruto.resize((150, 150), Image.ANTIALIAS)

imgFairytail = Image.open("fairytail.jpg")
imgFairytail = imgFairytail.resize((150, 150), Image.ANTIALIAS)

imgOnePiece = Image.open("onepiece.jpg")
imgOnePiece = imgOnePiece.resize((150, 150), Image.ANTIALIAS)

bleach = ImageTk.PhotoImage(imgBleach)
dragonball = ImageTk.PhotoImage(imgDragonBall)
fairytail = ImageTk.PhotoImage(imgFairytail)
naruto = ImageTk.PhotoImage(imgNaruto)
onepiece = ImageTk.PhotoImage(imgOnePiece)

labelBleach = Label(root, image=bleach)
labelDragonBall = Label(root, image=dragonball)
labelNaruto = Label(root, image=naruto)
labelOnePiece = Label(root, image=onepiece)
labelFairyTail = Label(root, image=fairytail)


labelBleach.grid(row = 1,column = 1)
labelOnePiece.grid(row = 1,column = 2)
labelNaruto.grid(row = 1,column = 3)
labelDragonBall.grid(row = 1,column = 4)
labelFairyTail.grid(row = 1,column = 5)



tk.Radiobutton(root,
              text="Bleach",
              padx = 20,
              variable=v,
              value=1).grid(row = 2,column = 1)

tk.Radiobutton(root,
              text="One Piece",
              padx = 20,
              variable=v,
              value=2).grid(row = 2 , column = 2)

tk.Radiobutton(root,
              text="Naruto",
              padx = 20,
              variable=v,
              value=3).grid(row = 2 , column = 3)

tk.Radiobutton(root,
              text="Dragon Ball",
              padx = 20,
              variable=v,
              value=4).grid(row = 2 , column = 4)

tk.Radiobutton(root,
              text="Fairy Tail",
              padx = 20,
              variable=v,
              value=5).grid(row = 2 , column = 5)

B = tk.Button(root, text ="Vote", command = SimpanVoting)
B.grid(row = 3,column = 3)


root.mainloop()


