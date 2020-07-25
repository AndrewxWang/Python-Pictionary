from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import PIL
import os
import time
root = Tk()
root.title("Pictionary")
root.geometry("675x400")
finalCount = 0
while True:
    finalCount = input("How many rounds would you like to have? (even number): ")
    if finalCount.isdigit() and int(finalCount)%2 == 0:
        print("<------------------>")
        break
    else:
        print("Enter a number (even number): ")
print("Instructions:")
print("Player 1 draws an object of their choice and enters the answer in the input box")
print("Player 2 tries to guess the object; if they guess correctly, the get a point")
print("Then, player 2 has to draw and Player 1 has to guess; this repeats for " + str(finalCount) + " round(s).")
print("The player with the most points wins!")
input("When you are ready, push \"enter\" to start!")
print("")

root.lift()
player = 1
inputAns = Entry(root)
inputGuess = Entry(root)
answer = StringVar()
guess = StringVar()
answers=[]
count=0
scoreOne = 0
scoreTwo = 0
img = PIL.Image.new("RGB", (250, 300), "gainsboro")
label = Label(root,bg="gainsboro", font=("Arial", 13))
oneScore = Label(root,bg="gainsboro", font=("Arial", 13))
twoScore = Label(root,bg="gainsboro", font=("Arial", 13))
roundCount= Label(root,bg="gainsboro", font=("Arial", 13))
clearBtn = Button(root, text="clear", state="normal", command=lambda:clearCanvas())
draw = ImageDraw.Draw(img)
    
def checkAnswer():
    global answers
    global count
    print("Answer: " + answers[count])
    if answers[count].lower() == guess.get().lower():
        correctAns()
    else:
        wrongAns()
    count+=1

def clearCanvas():
    global canvas
    canvas.delete("all")

def destroyWidgets(answerLabel, nextBtn):
    if answerLabel.winfo_exists() == 1:
        answerLabel.destroy()
    if nextBtn.winfo_exists() == 1:
        nextBtn.destroy()
        
def correctAns():
    global scoreOne, scoreTwo
    answerLabel = Label(text="Correct Answer!")
    answerLabel.place(x=300,y=200)
    nextBtn = Button(root, text="next", command=lambda:[createImage(), destroyWidgets(answerLabel,nextBtn)])
    nextBtn.place(x=325,y=240)
    canvas.create_rectangle(0, 0, 300, 250, fill="green", outline="green")
    if player == 1:
        scoreTwo+=1
    else:
        scoreOne+=1
        
def wrongAns():
    global scoreOne, scoreTwo
    answerLabel = Label(text="Wrong Answer!")
    answerLabel.place(x=300,y=200)
    nextBtn = Button(root, text="next", command=lambda:[createImage(), destroyWidgets(answerLabel,nextBtn)])
    nextBtn.place(x=325,y=240)
    canvas.create_rectangle(0, 0, 300, 250, fill="red", outline="red")
    
    if player == 1:
        scoreOne+=1
    else:
        scoreTwo+=1
        
def deleteEntry():
    inputAns.delete(0,END)
    inputGuess.delete(0,END)
    
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black",width=10)
    draw.line([x1, y1, x2, y2],fill="black",width=5)

def changePlayer():
    global player, count
    if count%2 == 0:
        player = 1
    else:
        player = 2

def printWinner():
    global scoreOne, scoreTwo
    print("Player 1: " + str(scoreOne))
    print("Player 2: " + str(scoreTwo))
    winner = Canvas(root, bg="gainsboro", height=1920, width=1080)
    winner.place(x=0,y=0)
    finalScore = ""
    if scoreOne > scoreTwo:
        finalScore = 1
    elif scoreTwo > scoreOne:
        finalScore = 2
    else:
        finalScore = -1

    if finalScore == -1:
        winnerLab = Label(root, text="THERE IS A TIE!", font=("Arial",13))
        winnerLab.place(x=250,y=200)
    else:
        winnerLab = Label(root, text="PLAYER " + str(finalScore) + " WINS ☺", font=("Arial",13))
        winnerLab.place(x=250,y=200)

def saveAns():
    answers.append(answer.get())
    userAnswer()

def createImage():
    global inputAns, label, clearBtn
    global finalCount
    global canvas
    changePlayer()
    deleteEntry()
    clearCanvas()
    canvas.configure(bg="gainsboro")
    canvas.bind("<B1-Motion>", paint)
    oneScore.configure(text="Player 1: " + str(scoreOne))
    twoScore.configure(text="Player 2: " + str(scoreTwo))
    oneScore.place(x=10,y=100)
    twoScore.place(x=10,y=130)
    roundCount.configure(text="Round: " + str(count+1))
    roundCount.place(x=600,y=350)
    label.configure(text="Player " + str(player) + "'s drawing!")
    label.pack(pady=10)
    enterAns = Label(root, text="Enter answer: ")
    enterAns.place(x=220,y=60)
    submit = Button(root, text="submit", state="normal", command=lambda: saveAns())
    submit.place(x=310,y=360)
    inputAns = Entry(root, bd=5, textvariable=answer)
    inputAns.config(show="*");
    inputAns.place(x=310,y=60)
    clearBtn['state'] = NORMAL
    clearBtn.place(x=10,y=360)
    if count == int(finalCount):
        printWinner()            
         
def disableButton(button):
    button['state'] = DISABLED

def checkGuessing():
    global label
    if (player == 1):
        label.configure(text="Player 2's guessing!")
    else:
        label.configure(text="Player 1's guessing!")

def userAnswer():
    global canvas, inputGuess
    changePlayer()
    deleteEntry()
    clearBtn['state'] = DISABLED
    canvas.unbind("<B1-Motion>")
    checkGuessing()
    enterGuess = Label(root, text="Guess image: ")
    enterGuess.place(x=220,y=60)
    inputGuess = Entry(root, bd=5, textvariable=guess)
    inputGuess.place(x=310,y=60)
    guessBtn = Button(root, text=" guess ", command=lambda:[ checkAnswer(), disableButton(guessBtn)])
    guessBtn.place(x=310,y=360)

canvas = Canvas(root, bg="gainsboro", height=250, width=300)
canvas.pack(side=BOTTOM, pady=50)
createImage()  
root.mainloop()
