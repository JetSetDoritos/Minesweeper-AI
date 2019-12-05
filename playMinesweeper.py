from Minesweeper import Minesweeper

mines = int(input("Enter mines.."))
size = int(input("Grid size.."))
g = Minesweeper(size,mines)

g.playMinesweeper()