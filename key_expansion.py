from time import sleep
from random import randint


def key_expansion(grid, key, col, sub, col2, xor, board):
    sub.set_show(True)
    sub.set_location(11, key.get_cell_location()[1])
    board.set_text("Starting Key Expansion")

    col2.set_show(True)
    col2.set_values([2, 0, 0, 0])
    col2.set_location(14, key.get_cell_location()[1])

    key.start()
    for _ in range(3):
        key.move_one()
    key.stop()
    sleep(0.5)

    board.set_text("creating copy of last column")
    col.set_values([key.values[i * 4 + 3] for i in range(4)])
    loc = key.get_cell_location()
    col.set_location(loc[0]+3, loc[1])
    col.set_show(True)

    col.set_direction(0)
    for _ in range(2):
        col.move_one()

    board.set_2_line_text(["rotating column in", "upward direction"])
    sleep(0.3)
    col.shift_down()
    sleep(0.8)

    for _ in range(2):
        col.move_one()

    board.set_2_line_text(["passing the column through", "a substitution layer"])
    sleep(0.6)
    new_val = [randint(0, 255) for _ in range(4)]
    sub.show_sub(new_val, col.values)
    col.set_values(new_val)
    sleep(0.6)
    sub.set_show(False)

    col.move_one()
    col.move_one()

    board.set_2_line_text(["XORing round const to", "the result"])
    col2.set_direction(2)
    col2.move_one()

    xor.set_show(True)
    xor.set_location(13, key.get_cell_location()[1])
    curr_values = col.values.copy()
    col.set_values(xor.show_xor(curr_values, [2, 0, 0, 0]))
    col2.set_show(False)
    sleep(0.8)
    xor.set_show(False)

    # col2.set_direction(0)
    # col2.move_one()

    col.set_direction(3)
    for _ in range(5):
        col.move_one()

    # col2.set_show(False)
    # sub.set_show(False)
    board.set_2_line_text(["XORing result with first column", "of the previous round key"])
    key.start()
    for _ in range(9):
        key.move_one()

    col.set_direction(1)
    for _ in range(5):
        col.move_one()

    loc = key.get_cell_location()
    col.set_direction(0)

    xor.set_show(True)
    xor.set_location(loc[0], loc[1])
    new_values = xor.show_xor([key.values[i * 4] for i in range(4)], col.values.copy())
    sleep(0.5)
    xor.set_show(False)
    key.update_column(new_values, 0)
    col.set_values(new_values)
    col.move_one()

    board.set_2_line_text(["taking the result and", "XORing with next column"])
    xor.set_show(True)
    xor.set_location(loc[0]+1, loc[1])
    new_values = xor.show_xor([key.values[i * 4 + 1] for i in range(4)], col.values.copy())
    sleep(0.5)
    xor.set_show(False)
    key.update_column(new_values, 1)
    col.set_values(new_values)
    col.move_one()

    xor.set_show(True)
    xor.set_location(loc[0]+2, loc[1])
    new_values = xor.show_xor([key.values[i * 4 + 2] for i in range(4)], col.values.copy())
    sleep(0.5)
    xor.set_show(False)
    key.update_column(new_values, 2)
    col.set_values(new_values)
    col.move_one()

    xor.set_show(True)
    xor.set_location(loc[0]+3, loc[1])
    new_values = xor.show_xor([key.values[i * 4 + 3] for i in range(4)], col.values.copy())
    sleep(0.5)
    xor.set_show(False)
    key.update_column(new_values, 3)
    col.set_values(new_values)
    col.move_one()

    board.set_text("The new round key is Ready")
    col.set_direction(3)
    for _ in range(5):
        col.move_one()
    col.set_show(False)

    key.set_direction(0)
    for _ in range(5):
        key.move_one()
