import pygame
from time import sleep


class KeyCol(pygame.sprite.Sprite):

    def __init__(self, grid, values, x=2, y=2, size=50, speed=2):
        super().__init__()
        self.grid = grid
        self.values = values
        self.size = size
        self.location = [x * self.size, y * self.size]
        self.speed = speed
        self.is_stop = True
        self.direction = -1
        self.col = pygame.Surface([self.size, 4 * self.size])
        self.col.fill('#000000')
        self.show = True
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 25)

    def set_show(self, val):
        self.show = val

    def set_location(self, x, y):
        self.location = [x * self.size, y * self.size]

    def set_values(self, val):
        self.values = val

    def get_show(self):
        return self.show

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
        i = 0
        for j in range(4):
            curr_code = self.values[j]
            self.rect = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (curr_code, curr_code, curr_code), self.rect)
            number = self.font.render(str(curr_code), True, (255, 0, 0), None)
            rect = number.get_rect()
            rect.center = [(i + 0.5) * self.size, (j + 0.5) * self.size]
            self.col.blit(number, rect)

    def get_cell_location(self):
        return int(self.location[0] / self.size), int(self.location[1] / self.size)

    def get_location(self):
        return self.location[0], self.location[1]

    def move_left(self):
        self.location[0] -= self.speed

    def move_right(self):
        self.location[0] += self.speed

    def move_top(self):
        self.location[1] -= self.speed

    def move_down(self):
        self.location[1] += self.speed

    def shift_down(self):
        val = self.values[1:] + [self.values[0]]
        self.values = val.copy()

    def move_one(self):
        if self.direction == 0:
            next = (int(self.location[0] / self.size) + 1) * self.size
            while self.location[0] <= next:
                self.move_right()
                sleep(0.03)
            self.location[0] = next

        elif self.direction == 1:
            next = (int(self.location[1] / self.size) + 1) * self.size
            while self.location[1] <= next:
                self.move_down()
                sleep(0.03)
            self.location[1] = next

        elif self.direction == 2:
            next = (int(self.location[0] / self.size) - 1) * self.size
            while self.location[0] >= next:
                self.move_left()
                sleep(0.03)
            self.location[0] = next

        elif self.direction == 3:
            next = (int(self.location[1] / self.size) - 1) * self.size
            while self.location[1] >= next:
                self.move_top()
                sleep(0.03)
            self.location[1] = next

        # self.location = [int(self.location[0] / self.size * self.size), int(self.location[1] / self.size * self.si)]

