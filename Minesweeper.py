from Grid import Grid
from ast import literal_eval as make_tuple

class Minesweeper():
    def __init__(self,size=10,bombs=12):
        self.currGame = Grid(size,bombs)

    def getGrid(self):
        return self.currGame.gridArray
    def getCountGrid(self):
        return self.currGame.get_count_grid()
    def getExposedGrid(self):
        return self.currGame.get_exposed_grid()

    def playMinesweeper(self):

        while self.currGame.notDead() and self.currGame.notWon():
            self.currGame.printGrid()
            coords = input("Input coordinates as x,y: ")
            tupcoords = make_tuple("(" + coords + ")")
            self.currGame.revealTile(tupcoords[1],tupcoords[0])
            

        self.currGame.printRevealedGrid()