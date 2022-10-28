import pygame
from time import sleep


class Text(pygame.sprite.Sprite):
    def __init__(self, grid, values, x=2, y=2, size=50, speed=2, color='grey'):
        super().__init__()
        self.speed = speed
        self.cell_size = size
        self.values = list(values)
        self.text = pygame.Surface([4 * self.cell_size, 4 * self.cell_size])
        self.text.fill('#000000')
        self.grid = grid
        self.location = [x * self.cell_size, y * self.cell_size]
        self.is_stop = True
        self.direction = 0
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.show = True

    def set_location(self, x, y):
        self.location = [x * self.cell_size, y * self.cell_size]

    def get_show(self):
        return self.show

    def set_show(self, val):
        self.show = val

    def start(self):
        self.is_stop = False

    def stop(self):
        self.is_stop = True

    def set_direction(self, d):
        self.direction = d

    def move(self):
        if self.is_stop:
            return

        if self.direction == 0:
            self.move_right()
        elif self.direction == 1:
            self.move_down()
        elif self.direction == 2:
            self.move_left()
        elif self.direction == 3:
            self.move_top()

    def update_colors(self):
        for i in range(4):
            for j in range(4):
                curr_code = self.values[i+j*4]
                self.rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.text, (curr_code, curr_code, curr_code), self.rect)
                number = self.font.render(str(curr_code), True, (255, 0, 0), None)
                rect = number.get_rect()
                rect.center = [(i + 0.5) * self.cell_size, (j + 0.5) * self.cell_size]
                self.text.blit(number, rect)

    def update_values(self, x, y, n):
        self.values[x * 4 + y] = n

    def shift_rows(self):
        for j in range(4):
            i = j*4
            for _ in range(j):
                self.values[i:i + 4] = self.values[i + 1:i + 4] + [self.values[i]]
                sleep(0.5)
            sleep(0.5)

    def get_cell_location(self):
        return int(self.location[0] / self.cell_size), int(self.location[1] / self.cell_size)

    def get_location(self):
        return self.location[0],  self.location[1]

    def move_left(self):
        self.location[0] -= self.speed

    def move_right(self):
        self.location[0] += self.speed

    def move_top(self):
        self.location[1] -= self.speed

    def move_down(self):
        self.location[1] += self.speed


