import tkinter as tk
import numpy as np
import GameManager as gm

#Make a tkinter window
w = tk.Tk()
w.title("Minesweeper")
w.geometry("600x400")
w.minsize("600", "400")

#Frame for game configuration
infoFrame = tk.Frame(w)
infoFrame.pack(side="left", fill = "y", pady = 10, padx = 5)

#Frame for game button grid
gameFrame = tk.Frame(w)
gameFrame.pack(fill = "both", expand = "yes", padx=10, pady = 10)

gameLabel = tk.Label(infoFrame,text = "Minesweeper", font=("Arial", 20))
gameLabel.pack(side = "top")

gameSizeLabel = tk.Label(infoFrame,text = "Board size")
gameSizeLabel.pack()

#Create interactive widgets
sizeListBox = tk.Listbox(infoFrame, height = 3)
mineSpinBox = tk.Spinbox(infoFrame, from_ = 1, to = 25)
timeLabel = tk.Label(infoFrame,text = "Time: 0.00")
bestTimeLabel = tk.Label(infoFrame,text = "Best overall time: 0.00")

#Create main game manager
gameManager = gm.GM(w, gameFrame, sizeListBox, mineSpinBox, timeLabel, bestTimeLabel)

#Add different board sizes to list box
for x in range(len(gameManager.gameSizeList)):
    sizeListBox.insert(x, gameManager.gameSizeList[x])
sizeListBox.pack()

#Radio buttons for flag/selection selecting
selectionRadioButton1 = tk.Radiobutton(infoFrame, text = "Selection", variable = gameManager.selecting, value = True)
selectionRadioButton1.pack()
selectionRadioButton2 = tk.Radiobutton(infoFrame, text = "Flag", variable = gameManager.selecting, value = False)
selectionRadioButton2.pack()

mineLabel = tk.Label(infoFrame,text = "Mines amount")
mineLabel.pack()
mineSpinBox.pack()

bestTimeLabel.pack(side = "top")
timeLabel.pack(side = "top")

startButton = tk.Button(infoFrame, text="Start", width = 10, height = 2)
startButton.bind("<Button-1>", gameManager.StartButtonPressed)
startButton.pack(side="bottom", fill = "x")

w.mainloop()