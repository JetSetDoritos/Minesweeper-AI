from Grid import Grid

class Minesweeper():

    def playMinesweeper(self,size=10,bombs=12):
        currGame = Grid(size,bombs)


        while currGame.notDead():
            currGame.printGrid()
            #these are reversed on purpose
            y = int(input("Enter x coord: "))
            x = int(input("Enter y coord: "))
            currGame.revealTile(x,y)
            

        currGame.printRevealedGrid()