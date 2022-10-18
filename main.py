import random
import threading
import pygame.sprite
from objects.grid import Grid
from objects.text import Text
from gui import run_gui
from animation_logic import logic


# grid initialization
grid = Grid(100, 100, 50)
grid.initialize_grid()

text = Text(grid, [random.randint(0, 255) for i in range(16)], x=5, y=5, speed=2, size=grid.get_size())

if __name__ == '__main__':

    print('starting logical thread')
    threading.Thread(target=logic, args=[grid, text], daemon=True).start()

    print('starting the pygame windows')
    run_gui(grid, text)

