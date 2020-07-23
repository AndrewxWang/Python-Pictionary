from tkinter import *
from PIL import ImageTk,Image, ImageDraw
import PIL
import os
import pathlib

root = Tk()
root.title("Pictionary")
root.geometry("675x400")
inputAns = Entry(root)
answer = StringVar()
guess = StringVar()
answers=[]
count=0
img = PIL.Image.new("RGB", (250, 300), "gainsboro")
draw = ImageDraw.Draw(img)

def saveImg(img_name):
    global count
    global inputAns
    print(count)
    img_name.save(str(count) + ".png")
    answers.append(answer.get())
    print(answers)
    inputAns.delete(0,-1)
    userAnswer()
    
def openImage():
    global count
    global canvas
    image = Image.open(str(count) + ".png")
    img = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=img, anchor=NW)
    print("d")    
def checkAnswer():
    pass

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black",width=10)
    draw.line([x1, y1, x2, y2],fill="black",width=5)
    
def createImage():
    global inputAns
    canvas.create_rectangle(0, 0, 300, 250, fill="gainsboro", outline="gainsboro")
    canvas.bind("<B1-Motion>", paint)
    label = Label(root, text="Player: 1", bg="gainsboro", font=("Arial", 13))
    label.pack(pady=10)
    enterAns = Label(root, text="Enter answer: ")
    enterAns.place(x=220,y=60)
    inputAns = Entry(root, bd=5, textvariable=answer)
    inputAns.place(x=310,y=60)
    button = Button(root, text="submit", command=lambda: saveImg(img))
    button.place(x=310,y=360)

def removeWidgets(root):
    for widget in root.winfo_children():
        widget.destroy()
        
def userAnswer():
    global count
    global root
    global canvas
    canvas.create_rectangle(0, 0, 300, 250, fill="gainsboro", outline="gainsboro")
    canvas.unbind("<B1-Motion>")
    image = Image.open(str(count) + ".png")
    img = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=img, anchor=NW)
    
    enterGuess = Label(root, text="Guess image: ")
    enterGuess.place(x=220,y=60)
    inputGuess = Entry(root, bd=5, textvariable=guess)
    inputGuess.place(x=310,y=60)
    openImage()
    
    count+=1

canvas = Canvas(root, bg="gainsboro", height=250, width=300)
canvas.pack(side=BOTTOM, pady=50)
createImage()

    
#
#
#
#TEMP
path = pathlib.Path().absolute()
for fname in os.listdir(path):
        if fname.endswith('.png'):
            os.remove(fname)
#DELETES ALL IMAGES FROM FOLDER WHEN DONE
#NOTE: IF YOU WANT TO SAVE YOUR DRAWINGS, MOVE THEM INTO A DIFFERENT FOLDER
##if count == 6:
##    path = pathlib.Path().absolute()
##    for fname in os.listdir(path):
##        if fname.endswith('.png'):
##            os.remove(fname)
root.mainloop()
