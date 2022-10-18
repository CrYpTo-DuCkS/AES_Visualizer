import random
from time import sleep


def logic(grid, text):
    sleep(2)
    text.start()
    sleep(4)
    text.stop()
    text.shift_rows()
    text.start()
    sleep(4)
    text.stop()
    # while 1:
    #     # for i in range(1, 4):
    #     #     text.update_colors(0, i, )
    #     # text.update_values(random.randint(0, 4), random.randint(0, 4), random.randint(0, 255))
    #     # text.move_right()
    #     sleep(0.5)


