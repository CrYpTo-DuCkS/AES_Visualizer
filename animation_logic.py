import random
from time import sleep


def logic(grid, text):
    while 1:
        text.update_values(random.randint(0, 3), random.randint(0, 3), random.randint(0, 255))
        text.move_right()
        sleep(0.5)


