from Tile import Tile
import random

class Grid():
    def __init__(self,size=10,bombs=10):
        self.size = size
        self.bombs = bombs

        tempGridi = []
        for i in range(0,size):
            tempGridj = []
            for j in range(0,size):
                tempGridj.append(Tile())
            tempGridi.append(tempGridj)
        self.gridArray = tempGridi

        self.generateBombs()
        self.generateNumbers()

    def printGrid(self):
        print("Printing Grid State:")
        for i in range(0,self.size):
            for j in range(0,self.size):
                
                if self.gridArray[i][j].isRevealed():
                    print("[   ]", end='', flush=True)
                else:
                    print("[ # ]", end='', flush=True)
            print("")
    
    def printRevealedGrid(self):
        print("Printing Revealed State:")
        for i in range(0,self.size):
            for j in range(0,self.size):
                
                if self.gridArray[i][j].isBomb():
                    print("[ x ]", end='', flush=True)
                else:
                    if self.gridArray[i][j].getNearBombs() > 0:
                        print("[ "+ str(self.gridArray[i][j].getNearBombs()) +" ]", end='', flush=True)
                    else:
                        print("[   ]", end='', flush=True)
            print("")
    

    def generateBombs(self):
        bombsLocation = random.sample(range(0, self.size*self.size), self.bombs)
        print("Generating bombs " + str(self.bombs))
        tracker = 0
        for i in range(0,self.size):
            for j in range(0,self.size):
                if tracker in bombsLocation:
                    self.gridArray[i][j].setBomb()
                tracker+=1

    def generateNumbers(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                nearBombs = 0
                currTile = self.gridArray[i][j]
                if currTile.isBomb() == True:
                    continue
                if i > 0: #if not top row
                    if self.gridArray[i-1][j].isBomb():
                        nearBombs +=1
                    if j > 0:
                        if self.gridArray[i-1][j-1].isBomb():
                            nearBombs+=1
                    if j < self.size-1:
                        if self.gridArray[i-1][j+1].isBomb():
                            nearBombs+=1
                if j > 0:
                    if self.gridArray[i][j-1].isBomb():
                        nearBombs+=1
                if j < self.size - 1:
                    if self.gridArray[i][j+1].isBomb():
                        nearBombs+=1
                if i < self.size - 1:
                    if self.gridArray[i+1][j].isBomb():
                        nearBombs +=1
                    if j > 0:
                        if self.gridArray[i+1][j-1].isBomb():
                            nearBombs+=1
                    if j < self.size-1:
                        if self.gridArray[i+1][j+1].isBomb():
                            nearBombs+=1


                self.gridArray[i][j].setNearBombs(nearBombs)
                



                

