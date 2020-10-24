
class Tile:
    def __init__(self, number):
        self.number = number
        if number == -1:
            self.bomb = True
        else:
            self.bomb = False
            
        self.revealed = False




