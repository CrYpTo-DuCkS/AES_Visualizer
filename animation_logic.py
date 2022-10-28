import random
from time import sleep

from key_expansion import key_expansion


def logic(grid, text, col, key, sub, col2, xor, board):
    # sleep()
    key_expansion(grid, key, col, sub, col2, xor, board)
    # col.start()
    #
    # for i in range(4):
    #     for j in range(4):
    #         col.set_direction(j)
    #         col.move_one()
    #
    # # while col.get_cell_location()[0] < 6:
    # #     col.move()
    # #     sleep(0.03)
    # #
    # # col.set_direction(3)
    # #
    # # while col.get_cell_location()[0] > 0:
    # #     col.move()
    # #     sleep(0.03)
    # sleep(2)
    # text.start()
    # sleep(4)
    # text.stop()
    # text.shift_rows()
    # text.start()
    # sleep(4)
    # text.stop()
    # # while 1:
    # #     # for i in range(1, 4):
    # #     #     text.update_colors(0, i, )
    # #     # text.update_values(random.randint(0, 4), random.randint(0, 4), random.randint(0, 255))
    # #     # text.move_right()
    # #     sleep(0.5)


