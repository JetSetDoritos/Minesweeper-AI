

class Tile():
    def __init__(self,bomb=False):
        self.bomb = False
        self.revealed = False
        self.nearBombs = 0

    def isBomb(self):
        return self.bomb

    def isRevealed(self):
        return self.revealed
    
    def setBomb(self):
        self.bomb=True
    
    def setNearBombs(self,near = 0):
        self.nearBombs = near
    
    def getNearBombs(self):
        return self.nearBombs

    def revealTile(self):
        self.revealed = True

    def printer(self):
        if self.revealed:
            if(self.bomb):
                return "x"
            if self.nearBombs == 0:
                return " "
            else:
                return str(self.nearBombs)
        else:
            return "#"

    def debugPrinter(self):
        if self.bomb:
            return "x"
        if self.nearBombs == 0:
            return " "
        else:
            return str(self.nearBombs)

    