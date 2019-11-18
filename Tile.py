

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
    