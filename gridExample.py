from Minesweeper import Minesweeper

g = Minesweeper(10,8)

print(g.getGame().get_exposed_grid())
print(g.getGame().get_count_grid())
g.getGame().printGrid()
g.getGame().printRevealedGrid()
