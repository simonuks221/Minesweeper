import tkinter as tk
import numpy as np

class GM:
    gameSizeList = ["5x5", "10x10", "10x5"]
    tileArray = None

    def __init__(self, gameFrame, sizeListBox):
        self.gameFrame = gameFrame
        self.sizeListBox = sizeListBox

    def GenerateTileGrid(self):
        for y in range(self.tileArray.shape[0]):
            for x in range(self.tileArray.shape[1]):
                newButton = tk.Button(self.gameFrame, height = 1, width = 2)
                newButton.grid(row = x, column = y)

    def GenerateTiles(self):
        for y in range(self.tileArray.shape[0]):
            for x in range(self.tileArray.shape[1]):
                self.tileArray[y, x] = int(0)


    def StartButtonPressed(self, event):
        size = self.gameSizeList[self.sizeListBox.curselection()[0]]
        sizeX = int(size.split("x")[0])
        sizeY = int(size.split("x")[1])

        self.tileArray = np.empty([sizeX, sizeY])
        self.GenerateTiles()
        self.GenerateTileGrid()
        
