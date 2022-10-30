import random
from time import sleep

from key_expansion import key_expansion


def logic(grid, text, col, key, sub, col2, xor, board, xor_key, sub_bytes):
    # sleep()
    key_expansion(grid, key, col, sub, col2, xor, board)
    text.set_show(True)
    # col.start()
    
    # for i in range(4):
    #     for j in range(4):
    #         col.set_direction(j)
    #         col.move_one()
    
    # while col.get_cell_location()[0] < 6:
    #     col.move()
    #     sleep(0.03)
    
    # col.set_direction(3)
    
    # while col.get_cell_location()[0] > 0:
    #     col.move()
    #     sleep(0.03)

    board.set_2_line_text(["Step 1: Add Round Key", ""])
    text.start()
    key.start()
    key.set_direction(1)
    for _ in range(5):
        key.move_one()

    for _ in range(4):
        text.move_one()

    for i in range(4):
        xor_key[i].set_show(True)
    
    key.stop()
    text.stop()

    # for i in range(4):
    #     new_values = xor_key[i].show_xor([text.values[0+i],text.values[4+i],text.values[8+i],text.values[12+i]],[key.values[0+i],key.values[4+i],key.values[8+i],key.values[12+i]])
    #     for j in range(4):
    #         text.update_values(j,i,new_values[j])

    # text.update_colors()
    text.add_round_key(key,xor_key)

    for i in range(4):
        xor_key[i].set_show(False)

    key.start()
    text.start()
    key.set_direction(3)
    for _ in range(5):
        key.move_one()

    for i in range(4):
        sub_bytes[i].set_show(True)
    
    board.set_2_line_text(["Step 2: Sub Bytes", ""])

    for _ in range(5):
        text.move_one()
    text.stop()

    # for i in range(4):
    #     new_values = sub_bytes[i].show_sub([text.values[0+i],text.values[4+i],text.values[8+i],text.values[12+i]])
    #     for j in range(4):
    #         text.update_values(j,i,new_values[j])

    # text.update_colors()
    text.sub_bytes(sub_bytes)

    text.start()
    board.set_2_line_text(["Step 3: Shift Rows", ""])
    for _ in range(5):
        text.move_one()
    text.stop()

    text.shift_rows()
    
    # while 1:
    #     for i in range(1, 4):
    #         text.update_colors()
    #     text.update_values(random.randint(0, 4), random.randint(0, 4), random.randint(0, 255))
    #     text.move_right()
    #     sleep(0.5)


