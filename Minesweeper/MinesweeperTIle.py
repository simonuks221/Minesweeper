#Tile class for storing game tile information
class Tile:
    button = None
    def __init__(self, number):
        self.number = number
        if number == -1:
            self.bomb = True
        else:
            self.bomb = False
        self.revealed = False
        self.flag = False




