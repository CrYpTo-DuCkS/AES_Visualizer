import random
import threading
import pygame.sprite
from objects.grid import Grid
from objects.text import Text
from objects.key_col import KeyCol
from objects.xor import Xor
from objects.sub import Sub
from objects.key import Key
from objects.board import Board
from gui import run_gui
from animation_logic import logic


# grid initialization
grid = Grid(100, 100, 50)
grid.initialize_grid()

text = Text(grid, [random.randint(0, 255) for _ in range(16)], x=5, y=5, speed=2, size=grid.get_size())
key = Key(grid, [random.randint(0, 255) for _ in range(16)], x=1, y=7, speed=2, size=grid.get_size())
col = KeyCol(grid, [random.randint(0, 255) for _ in range(16)], x=5, y=5, speed=2, size=grid.get_size())
xor = Xor(grid, [random.randint(0, 255) for _ in range(16)], x=5, y=5, speed=2, size=grid.get_size())
sub = Sub(grid, [random.randint(0, 255) for _ in range(16)], x=5, y=5, speed=2, size=grid.get_size())
col2 = KeyCol(grid, [random.randint(0, 255) for _ in range(16)], x=5, y=5, speed=2, size=grid.get_size())
board = Board(11, 0, grid.get_size())

col.set_show(False)
col2.set_show(False)
xor.set_show(False)
sub.set_show(False)

if __name__ == '__main__':

    print('starting logical thread')
    threading.Thread(target=logic, args=[grid, text, col, key, sub, col2, xor, board], daemon=True).start()

    print('starting the pygame windows')
    run_gui(grid, text, col, key, sub, col2, xor, board)

