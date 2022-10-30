import pygame
from sys import exit
from objects.camera import Camera


def get_object_location(obj_loc, camera_offset):
    return obj_loc[0] + camera_offset[0], obj_loc[1] + camera_offset[1]


def run_gui(grid, text, col, key, sub, col2, xor, board, xor_key, sub_bytes):
    pygame.init()
    screen = pygame.display.set_mode((1500, 900))
    clock = pygame.time.Clock()

    # camera initialization
    camera = Camera(30, grid, 1200, 700)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                camera.reset()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                camera.change()

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            #     camera.switch_camera_type()

        if grid.force_stop is True:
            exit(1)
        screen.fill('black')
        camera.update()
        screen.blit(grid.grid, camera.offset)
        screen.blit(board.board, get_object_location(board.get_location(), [0, 0]))


        if text.get_show():
            screen.blit(text.text, get_object_location(text.get_location(), camera.offset))
            text.update_colors()

        if key.get_show():
            screen.blit(key.key, get_object_location(key.get_location(), camera.offset))
            key.update_colors()

        if col.get_show():
            screen.blit(col.col, get_object_location(col.get_location(), camera.offset))
            col.update_colors()
            # col.move()

        if col2.get_show():
            screen.blit(col2.col, get_object_location(col2.get_location(), camera.offset))
            col2.update_colors()

        if sub.get_show():
            screen.blit(sub.sub, get_object_location(sub.get_location(), camera.offset))

        if xor.get_show():
            screen.blit(xor.col, get_object_location(xor.get_location(), camera.offset))

        for i in range(4):
            if xor_key[i].get_show():
                screen.blit(xor_key[i].col, get_object_location(xor_key[i].get_location(), camera.offset))

        for i in range(4):
            if sub_bytes[i].get_show():
                screen.blit(sub_bytes[i].col, get_object_location(sub_bytes[i].get_location(), camera.offset))

        pygame.display.flip()
        clock.tick(32)
