import numpy as np 
from Minesweeper import Minesweeper
#import Agent as Agent

rng = np.random.RandomState(123)

print(rng)

W = rng.uniform(low=-1e-5,high=1e-5,
            size=[8 * 8, 
                8 * 8 * 10])

print(W)

game= Minesweeper(10,8)
#state= np.asarray([[None]*8]*8)
state = game.getCountGrid()

cells = np.reshape(np.asarray(state),-1)
print(cells)
cells[np.isnan(cells.astype(float))]=9
print(cells)

extractedState = np.reshape(np.eye(10)[np.asarray(cells,'int')],[-1])

print(extractedState)
print(extractedState.shape[0])

print(set())