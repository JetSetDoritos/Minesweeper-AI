import numpy as np 
from Minesweeper import Minesweeper


class Agent():
    def __init__(self,width,height,bombs,game,config):
        self.iteration = 0
        self.iterations2 = 0
        self.wins = 0
        self.width = width
        self.height = height
        self.bombs = bombs

        self.config = config
        self.game = game
        self.rand = np.random.RandomState(1337)

        self.actionsId   = np.arange(self.width * self.height) ###
        self.W = self.rand.uniform(low=-1e-5,high=1e-5, 
                 size=[self.width * self.height, 
                        self.width * self.height * self.cellsStateCount])
        self.b = np.zeros([self.width * self.height])  

        state = self.game.getCountGrid()

        cells = np.reshape(np.asarray(state),-1)
        print(cells)
        cells[np.isnan(cells.astype(float))]=9
        print(cells)

        self.extractedState = np.reshape(np.eye(10)[np.asarray(cells,'int')],[-1])

        #self.inputDic = inputDic
        self.discountFactor = 0.9
        self.epsilonProb    = 0.2
        self.memorySize     = 1000000
        self.alpharidge     = 0.001

        self.prevState =np.zeros([self.memorySize,self.extractedState.shape[0]])
        self.prevAction=np.zeros([self.memorySize])
        self.prevTarget=np.zeros([self.memorySize])

    def tileMoveState(self):

        self.prevState[self.iterations2,:] = self.extractedState

        #result,newTile = self.selectEpsilonGreedy(self.extractedState)

    def selectEpsilonGreedy(self,gridState):
        Q = np.dot(self.W,gridState)+self.b

        maxAction = self.rand.binomial(n=1,p=1-self.epsilonProb,size=1)[0]

    
    def parseAction(self,Q,maxAction):
        exp = np.reshape(np.asarray(self.game.getExposedGrid()),-1)
        tmp = np.asarray(np.logical_not(exp),'float')
        Q[]