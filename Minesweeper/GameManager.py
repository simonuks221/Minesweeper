import tkinter as tk
import numpy as np
from MinesweeperTIle import Tile
from tkinter import messagebox

class GM:
    gameSizeList = ["5x5", "10x10", "10x5"]
    tileArray = np.ndarray((1, 1), dtype = np.object)

    def __init__(self, gameFrame, sizeListBox, mineSpinBox):
        self.gameFrame = gameFrame
        self.sizeListBox = sizeListBox
        self.mineSpinBox = mineSpinBox

    def GenerateTileGrid(self, showAll = False):
        for y in range(self.tileArray.shape[0]):
            for x in range(self.tileArray.shape[1]):
                if showAll:
                    print("TREU")
                    newButton = tk.Button(self.gameFrame,text = self.tileArray[y, x].number, height = 1, width = 2)
                else:
                    if self.tileArray[y, x].revealed:
                        newButton = tk.Button(self.gameFrame,text = self.tileArray[y, x].number, height = 1, width = 2)
                    else:
                        newButton = tk.Button(self.gameFrame, height = 1, width = 2)

                newButton.grid(row = y, column = x)
                newButton.bind("<Button-1>", lambda event, a = x, b = y: self.TileButtonPressed(a, b))


    def Isbomb(self, x, y):
        if(x >= 0 and y >= 0 and x < self.tileArray.shape[1] and y < self.tileArray.shape[0]):
            if(self.tileArray[y, x] == None):
                return False
            else:
                return self.tileArray[y, x].bomb
        return False

    def GenerateTiles(self):
        #Generate random bombs
        #TODO: chck if already bomb before placing
        for a in range(int(self.mineSpinBox.get())):
            x = np.random.randint(0, self.tileArray.shape[1])
            y = np.random.randint(0, self.tileArray.shape[0])
            self.tileArray[y, x] = Tile(-1)

        #Fill voids with numbers
        for y in range(0, self.tileArray.shape[0]):
            for x in range(0, self.tileArray.shape[1]):
                if(self.tileArray[y, x] == None):
                    neighbourBombs = 0
                    for yy in range(-1, 2):
                        for xx in range(-1, 2):
                            if(self.Isbomb(x + xx, y + yy)):
                                neighbourBombs += 1
                    self.tileArray[y, x] = Tile(neighbourBombs)
                    

    

    def StartButtonPressed(self, event):
        if len(self.sizeListBox.curselection()) == 1:  #Check if board size is selected
            size = self.gameSizeList[self.sizeListBox.curselection()[0]]
            sizeX = int(size.split("x")[0])
            sizeY = int(size.split("x")[1])

            self.tileArray = np.ndarray((sizeY, sizeX), dtype=np.object)
            self.GenerateTiles()
            self.GenerateTileGrid()

    def GameOver(self):
        self.GenerateTileGrid(True)
        tk.messagebox.showerror(title="Game over", message="You lost")
        
    def TileButtonPressed(self, x, y):
        if self.tileArray[y, x].bomb:
            self.GameOver()

        self.tileArray[y, x].revealed = True
        self.GenerateTileGrid()
        
