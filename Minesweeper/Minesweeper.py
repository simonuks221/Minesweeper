import tkinter as tk
import numpy as np
import GameManager as gm



selecting = True

w = tk.Tk()
w.title("Minesweeper")
w.geometry("500x300")

infoFrame = tk.Frame(w)
sizeListBox = tk.Listbox(infoFrame)
gameFrame = tk.Frame(w)
gameManager = gm.GM(gameFrame, sizeListBox)


infoFrame.pack(side="left")


gameFrame.pack()

gameLabel = tk.Label(infoFrame,text = "Minesweeper")
gameLabel.pack()


for x in range(len(gameManager.gameSizeList)):
    sizeListBox.insert(x, gameManager.gameSizeList[x])
sizeListBox.pack()

selectionRadioButton1 = tk.Radiobutton(infoFrame, text = "Selection", variable = selecting, value = True)
selectionRadioButton1.pack()
selectionRadioButton2 = tk.Radiobutton(infoFrame, text = "Flag", variable = selecting, value = False)
selectionRadioButton2.pack()

startButton = tk.Button(infoFrame, text="Start", width = 10, height = 2)
startButton.bind("<Button-1>", gameManager.StartButtonPressed)
startButton.pack()


w.mainloop()