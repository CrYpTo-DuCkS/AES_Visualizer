import pygame
import numpy as np


class Grid:
    def __init__(self, rows=100, columns=100, size=20):
        self.rows = rows
        self.cols = columns
        self.size = size
        self.grid = pygame.Surface([rows * size, columns * size])
        self.grid.fill('#bfeff5')
        self.matrix = np.zeros((rows, columns))
        self.force_stop = False

    def get_size(self):
        return self.size

    def initialize_grid(self):
        n = self.rows * self.size
        m = self.cols * self.size
        # for i in range(0, n + 1, self.size):
        #     pygame.draw.line(self.grid, '#9bc6cc', (0, i), (n, i))
        #     for j in range(0, m + 1, self.size):
        #         pygame.draw.line(self.grid, '#9bc6cc', (j, 0), (j, m))

    def force_stop(self):
        self.force_stop = True


