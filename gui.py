import pygame
from sys import exit
from objects.camera import Camera


def get_object_location(obj_loc, camera_offset):
    return obj_loc[0] + camera_offset[0], obj_loc[1] + camera_offset[1]


def run_gui(grid, text):
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
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

        screen.blit(text.text, get_object_location(text.get_location(), camera.offset))
        text.update_colors()
        text.move()

        pygame.display.flip()
        clock.tick(32)
