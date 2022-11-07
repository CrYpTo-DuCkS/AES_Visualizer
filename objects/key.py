import pygame
from time import sleep

from .text import Text


class Key(Text):

    def __init__(self, grid, values, x=2, y=2, size=50, speed=2, color='grey'):
        super().__init__(grid, values, x, y, size, speed, color)
        self.key = self.text
        self.is_key = 1

    def update_column(self, arr, col):
        for i in range(4):
            self.values[i*4+col] = arr[i]

    def move_one(self):
        self.size = self.cell_size

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
