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

        self.winState = False
        self.deadState = False
    
    def get_count_grid(self):
        tempGridi = []
        for i in range(0,self.size):
            tempGridj = []
            for j in range(0,self.size):
                currTile = self.gridArray[i][j]
                if(currTile.isRevealed()):
                    tempGridj.append(currTile.nearBombs)
                else:
                    tempGridj.append(None)
                
            tempGridi.append(tempGridj)
        return tempGridi
    
    def get_exposed_grid(self):
        tempGridi = []
        for i in range(0,self.size):
            tempGridj = []
            for j in range(0,self.size):
                currTile = self.gridArray[i][j]
                tempGridj.append(currTile.isRevealed())
                
            tempGridi.append(tempGridj)
        return tempGridi

    def printGrid(self):
        print("Printing Grid State:")
        print("[:) ]", end='', flush=True)
        for i in range(0,self.size):
            if i > 9:
                print("[ " + str(i) + "]", end='', flush=True)
            else:
                print("[ " + str(i) + " ]", end='', flush=True)
        print("")
        for i in range(0,self.size):
            if i > 9:
                print("[ " + str(i) + "]", end='', flush=True)
            else:
                print("[ " + str(i) + " ]", end='', flush=True)
            for j in range(0,self.size):
                print("[ " + self.gridArray[i][j].printer() + " ]", end='', flush=True) 
            print("")
    
    def printRevealedGrid(self):
        print("Printing Revealed State:")
        print("[:) ]", end='', flush=True)
        for i in range(0,self.size):
            if i > 9:
                print("[ " + str(i) + "]", end='', flush=True)
            else:
                print("[ " + str(i) + " ]", end='', flush=True)    
        print("")    
        for i in range(0,self.size):
            if i > 9:
                print("[ " + str(i) + "]", end='', flush=True)
            else:
                print("[ " + str(i) + " ]", end='', flush=True)
            for j in range(0,self.size):
                print("[ " + self.gridArray[i][j].debugPrinter() + " ]", end='', flush=True)
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

    def isEmpty(self,x,y):
        if self.gridArray[x][y].getNearBombs() > 0:
            self.gridArray[x][y].revealTile()
        if not(self.gridArray[x][y].isBomb()) and (self.gridArray[x][y].getNearBombs() <=1):
            if not self.gridArray[x][y].isRevealed():
                return True
        else:
            return False

    def revealTile(self,x,y):
        currTile = self.gridArray[x][y]

        if self.deadState:
            print("Your are dead :(")
        elif self.isEmpty(x,y):
            self.revealTileHelper(x,y)
        elif currTile.isBomb():
            currTile.revealTile()
            self.deadState = True
            print("Oh no! You hit a Bomb  💣 ")
        elif currTile.getNearBombs() == 0:
            self.revealTileHelper(x,y)
        else:
            currTile.revealTile()
        if self.verifyBombs():
            self.winState = True
        if self.winState:
            print("You have won! B)")
            return
        
        
        


    #assumes the tile at i,j is able to be revealed (isEmpty == True)
    #reveals the given (i,j) tile and checks if nearby tiles can be revealed
    def revealTileHelper(self,i,j):
        self.gridArray[i][j].revealTile()
        if i > 0: #if not top row
            if self.isEmpty(i-1,j):
                self.revealTileHelper(i-1,j)
            if j > 0:
                if self.isEmpty(i-1,j-1):
                    self.revealTileHelper(i-1,j-1)
            if j < self.size-1:
                if self.isEmpty(i-1,j+1):
                    self.revealTileHelper(i-1,j+1)
        if j > 0:
            if self.isEmpty(i,j-1):
                self.revealTileHelper(i,j-1)
        if j < self.size - 1:
            if self.isEmpty(i,j+1):
                self.revealTileHelper(i,j+1)
        if i < self.size - 1:
            if self.isEmpty(i+1,j):
                self.revealTileHelper(i+1,j)
            if j > 0:
                if self.isEmpty(i+1,j-1):
                    self.revealTileHelper(i+1,j-1)
            if j < self.size-1:
                if self.isEmpty(i+1,j+1):
                    self.revealTileHelper(i+1,j+1)
                
    def notDead(self):
        return not self.deadState
    def notWon(self):
        return not self.winState

    #verifies Bombs are the only tiles remaining
    #returns true if the only spaces left are bombs
    def verifyBombs(self):
        for ta in self.gridArray:
            for t in ta:
                if (t.isRevealed() == False) and (t.isBomb() == False): #if a space is not revealed and it is not a bomb
                    return False
        
        return True
                

