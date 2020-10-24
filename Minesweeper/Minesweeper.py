import tkinter as tk
import numpy as np
import GameManager as gm

w = tk.Tk()
w.title("Minesweeper")
w.geometry("500x300")

infoFrame = tk.Frame(w)
infoFrame.pack(side="left", fill = "y")
sizeListBox = tk.Listbox(infoFrame, height = 3)
gameFrame = tk.Frame(w)
gameFrame.pack(fill = "x",)
mineSpinBox = tk.Spinbox(infoFrame, from_ = 1, to = 10)

gameManager = gm.GM(gameFrame, sizeListBox, mineSpinBox)

gameLabel = tk.Label(infoFrame,text = "Minesweeper", font=("Arial", 20))
gameLabel.pack(side = "top")


gameSizeLabel = tk.Label(infoFrame,text = "Board size")
gameSizeLabel.pack()

for x in range(len(gameManager.gameSizeList)):
    sizeListBox.insert(x, gameManager.gameSizeList[x])
sizeListBox.pack()

selectionRadioButton1 = tk.Radiobutton(infoFrame, text = "Selection", variable = gameManager.selecting, value = True)
selectionRadioButton1.pack()
selectionRadioButton2 = tk.Radiobutton(infoFrame, text = "Flag", variable = gameManager.selecting, value = False)
selectionRadioButton2.pack()



mineLabel = tk.Label(infoFrame,text = "Mines amount")
mineLabel.pack()
mineSpinBox.pack()

startButton = tk.Button(infoFrame, text="Start", width = 10, height = 2)
startButton.bind("<Button-1>", gameManager.StartButtonPressed)
startButton.pack(side="bottom")


w.mainloop()