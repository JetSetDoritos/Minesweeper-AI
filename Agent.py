import numpy as np 
from Minesweeper import Minesweeper
from sklearn.linear_model import Ridge


class Agent():
    def __init__(self,width,height,bombs,game):
        self.iteration = 0
        self.iterations2 = 0
        self.wins = 0
        self.width = width
        self.height = height
        self.bombs = bombs

        self.game = game
        self.rand = np.random.RandomState(1337)

        self.actionsId   = np.arange(self.width * self.height) ###
        self.W = self.rand.uniform(low=-1e-5,high=1e-5, 
                 size=[self.width * self.height, 
                        self.width * self.height * 10])
        self.b = np.zeros([self.width * self.height])  

        state = self.game.get_count_grid()

        cells = np.reshape(np.asarray(state),-1)
        cells[np.isnan(cells.astype(float))]=9

        self.extractedState = np.reshape(np.eye(10)[np.asarray(cells,'int')],[-1])

        #self.inputDic = inputDic
        self.discountFactor = 0.9
        self.epsilonProb    = 0.6
        self.memorySize     = 100
        self.alpharidge     = 0.001

        self.prevState =np.zeros([self.memorySize,self.extractedState.shape[0]])
        self.prevAction=np.zeros([self.memorySize])
        self.prevTarget=np.zeros([self.memorySize])
        print("Agent initialized.")

    def tileMoveState(self):
        print("Begining round.")
        self.prevState[self.iterations2,:] = self.extractedState

        result,newTile = self.selectEpsilonGreedy(self.extractedState)
        self.prevState[self.iterations2] = newTile
        print(result)
        #makes the selected move
        self.game.revealTile(result[0],result[1])
        print(self.game.printGrid())
        #grabs new state
        cells = np.reshape(np.asarray(self.game.get_count_grid()),-1)
        cells[np.isnan(cells.astype(float))]=9
        #checks if dead
        if not self.game.notDead():
            self.prevState[self.iterations2] = -10 #reward
            print(self.game.printGrid())
            self.game.gridRegen()
            self.iteration +=1
            print("Win Loss " + str(self.wins) + " - " + str(self.iteration-self.wins))

        else:
            self.extractedState = np.reshape(np.eye(10)[np.asarray(cells,'int')],[-1])
            maxQ = self.qFun(self.extractedState)
            if self.game.notWon(): #not win state
                self.prevTarget[self.iterations2] = 1 + self.discountFactor * maxQ
            else: #win state
                self.prevTarget[self.iterations2] = 10 + self.discountFactor * maxQ
                print(self.game.printGrid())
                self.game.gridRegen()
                self.wins +=1
                print("Win Loss " + str(self.wins) + " - " + str(self.iteration))
        self.iterations2 +=1
        print(self.iterations2)
        if self.iterations2 == self.memorySize:
            self.updateModel()
            self.iterations2 = 0




        

    def selectEpsilonGreedy(self,gridState):
        print("Getting greedy move")
        Q = np.dot(self.W,gridState)+self.b

        maxAction = self.rand.binomial(n=1,p=1-self.epsilonProb,size=1)[0]

        selectMove = self.parseAction(Q,maxAction)

        coords = int(selectMove/self.width),int(selectMove%self.width)

        return (coords,selectMove)
        #*coords tuple with x and y for move

        

    
    def parseAction(self,Q,maxAction):
        exp = np.reshape(np.asarray(self.game.get_exposed_grid()),-1)
        tmp = np.asarray(np.logical_not(exp),'float')
        tmp[tmp==0] = -np.inf
        Q[exp] = np.abs(Q[exp])
        if maxAction:
            validActions = tmp*Q
            return np.argmax(validActions)
        else:
            temp2 = np.arange(len(self.actionsId))
            self.rand.shuffle(temp2)
            cnt = 0
            while(tmp[temp2[cnt]]==-np.inf):
                cnt +=1
            return temp2[cnt]
    
    def qFun(self,currState):
        Q=np.dot(self.W,currState)+self.b
        expo = np.reshape(np.asarray(self.game.get_exposed_grid()),-1)
        tmp = np.asarray(np.logical_not(expo),'float')
        tmp[tmp==0] = -np.inf
        Q[expo] = np.abs(Q[expo])
        validActionsQ = tmp*Q
        return np.max(validActionsQ)

    def updateModel(self):
        print("Updating model..")
        actionHistory = np.asarray(self.prevAction)
        for a in range(len(self.actionsId)):
            flag = actionHistory==a
            A = self.prevState[flag]             
            b = self.prevTarget[flag]

            if A.shape[0]>0:
                clf = Ridge(alpha=self.alpharidge)
                try:
                    #pdb.set_trace()
                    res= clf.fit(A, b.flatten())                    
                    self.W[k,:]   = res.coef_
                    self.b[k]     = res.intercept_
                except:
                    print()
        self.iteration+=1
        self.wins = 0


