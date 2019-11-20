from Grid import Grid
from ast import literal_eval as make_tuple

class Minesweeper():

    def playMinesweeper(self,size=10,bombs=12):
        currGame = Grid(size,bombs)


        while currGame.notDead() and currGame.notWon():
            currGame.printGrid()
            coords = input("Input coordinates as x,y: ")
            tupcoords = make_tuple("(" + coords + ")")
            currGame.revealTile(tupcoords[1],tupcoords[0])
            

        currGame.printRevealedGrid()