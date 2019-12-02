from Minesweeper import Minesweeper
import numpy as np

game = Minesweeper(12,18)

print (game.getGrid())

print(np.reshape(game.getCountGrid(),-1))

#game.playMinesweeper(12,18)