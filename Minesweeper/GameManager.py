import tkinter as tk
import numpy as np
from MinesweeperTIle import Tile
from tkinter import messagebox

class GM:
    gameSizeList = ["10x10", "15x15", "15x10"]
    tileArray = np.ndarray((1, 1), dtype = np.object)
    
    def __init__(self, root, gameFrame, sizeListBox, mineSpinBox, timeLabel, bestTimeLabel):
        self.root = root
        self.gameFrame = gameFrame
        self.sizeListBox = sizeListBox
        self.mineSpinBox = mineSpinBox
        self.timeLabel = timeLabel
        self.bestTimeLabel = bestTimeLabel
        self.selecting = tk.BooleanVar()
        self.selecting.set(True)
        self.flagsPlaced = 0
        self.time = 0
        self.timeRunning = False
        self.bestTimeLabel.configure(text = "Best overall time: " + str(self.GetBestTime()))


    def GetTileText(self, tile):
        if tile.bomb:
            return "*"
        elif tile.flag:
            return "F"
        else:
            return tile.number

    def GenerateTileGrid(self, showAll = False):
        for widget in self.gameFrame.winfo_children():
            widget.destroy()

        for y in range(self.tileArray.shape[0]):
            for x in range(self.tileArray.shape[1]):
                if showAll:
                    newButton = tk.Button(self.gameFrame,text = self.GetTileText(self.tileArray[y, x]), height = 1, width = 2)
                else:
                    if self.tileArray[y, x].revealed or self.tileArray[y, x].flag:
                        newButton = tk.Button(self.gameFrame,text = self.GetTileText(self.tileArray[y, x]), height = 1, width = 2)
                    else:
                        newButton = tk.Button(self.gameFrame, height = 1, width = 2)
                    newButton.bind("<Button-1>", lambda event, a = x, b = y: self.TileButtonPressed(a, b))
                newButton.grid(row = y, column = x)
                
    def ValidCoord(self, x, y):
        return x >= 0 and y >= 0 and x < self.tileArray.shape[1] and y < self.tileArray.shape[0]

    def Isbomb(self, x, y):
        if(self.ValidCoord(x, y)):
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
                    

    def UpdateClock(self):
        self.time += 0.01
        timeString = "Time: " + "%.2f" % self.time
        self.timeLabel.configure(text = timeString)
        if(self.timeRunning):
            self.root.after(10, self.UpdateClock)

    def StartButtonPressed(self, event):
        if len(self.sizeListBox.curselection()) == 1:  #Check if board size is selected
            self.flagsPlaced = 0
            size = self.gameSizeList[self.sizeListBox.curselection()[0]]
            sizeX = int(size.split("x")[0])
            sizeY = int(size.split("x")[1])

            self.tileArray = np.ndarray((sizeY, sizeX), dtype=np.object)
            self.GenerateTiles()
            self.GenerateTileGrid()

            self.time = 0
            self.timeRunning = True
            self.UpdateClock()

    def GetBestTime(self):
        try:
            f = open("highscore.txt", "r")
            highscore = f.read()
        except FileNotFoundError:
            f = open("highscore.txt", "w")
            highscore = str(100000000)
            f.write(highscore)
        finally:
            f.close()
            return highscore

    def GameOver(self, win):
        if win:
            self.timeRunning = False
            tk.messagebox.showinfo(title="Game over", message="You won. Time:  " + "%.2f" % self.time + " seconds")
            bestTime = self.GetBestTime()
            if self.time < float(bestTime):
                try:
                    f = open("highscore.txt", "w")
                    f.write(str( "%.2f" % self.time))
                    f.close()
                    self.bestTimeLabel.configure(text = "Best overall time: " + str(self.GetBestTime()))
                except OSError as err:
                    print("Error: ", err)
        else:
            tk.messagebox.showerror(title="Game over", message="You lost")
        self.GenerateTileGrid(True)

    def CheckWin(self):
        for y in self.tileArray:
            for x in y:
                if(x.bomb and not x.flag):
                    return False
        return True
        
    def TileButtonPressed(self, x, y):
        if self.selecting.get(): #Selecting tile
            if self.tileArray[y, x].bomb:
                self.GameOver(False)
            else:
                self.tileArray[y, x].revealed = True
                if self.tileArray[y, x].number == 0:
                    self.RevealEmptyTilesAround(x, y)
                
        else: #Placing flag
            if self.tileArray[y, x].flag:
                self.flagsPlaced -= 1
                self.tileArray[y, x].flag = False

            elif self.flagsPlaced < int(self.mineSpinBox.get()):
                self.tileArray[y, x].flag = True
                self.flagsPlaced += 1
                if self.CheckWin():
                    self.GameOver(True)
        self.GenerateTileGrid()
        

    def RevealEmptyTilesAround(self, x, y):
        for xx in range(-1, 2):
            for yy in range(-1, 2):
                if(self.ValidCoord(x + xx, y + yy)):
                    if(not self.tileArray[y + yy, x + xx].revealed):
                        self.tileArray[y + yy, x + xx].revealed = True
                        if self.tileArray[y + yy, x + xx].number == 0:
                            self.RevealEmptyTilesAround(x + xx, y + yy)