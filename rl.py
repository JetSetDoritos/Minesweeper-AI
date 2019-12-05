from Agent import Agent
from Minesweeper import Minesweeper

g = Minesweeper(10,8)
a = Agent(10,10,8,g.getGame())

while(True):
    a.tileMoveState()