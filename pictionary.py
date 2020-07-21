from tkinter import *
from PIL import ImageTk,Image
import os

root = Tk()
root.geometry("675x400")
imgs = []
#image 1
image1 = Image.open("img-1.png")
img1 = ImageTk.PhotoImage(image1)
imgs.append(img1)
#image 2
image2 = Image.open("img-2.png")
img2 = ImageTk.PhotoImage(image2)
imgs.append(img2)
#image 3
image3 = Image.open("img-3.png")
img3 = ImageTk.PhotoImage(image1)
imgs.append(img3)
#image 4
image4 = Image.open("img-4.png")
img4 = ImageTk.PhotoImage(image4)
imgs.append(img4)
#image 5
image5 = Image.open("img-5.png")
img5 = ImageTk.PhotoImage(image5)
imgs.append(img5)

print(imgs)
canvas = Canvas(root, bg="gainsboro", height=250, width=300)
canvas.create_image(0, 0, image=img1, anchor=NW)
canvas.pack(side=BOTTOM, pady=50)

def checkAnswer():
    pass

root.mainloop()
