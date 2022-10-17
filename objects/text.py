import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, grid, values, x=2, y=2, size=50, speed=2, color='grey'):
        super().__init__()
        # self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = grid.get_size()
        self.cell_size = grid.get_size()
        self.values = list(values)

        self.text = pygame.Surface([3 * self.cell_size, 3 * self.cell_size])
        self.text.fill('#000000')

        self.grid = grid

        self.location = [x, y]

    def update_colors(self):
        for i in range(3):
            for j in range(3):
                curr_code = self.values[i*3+j]
                self.rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.text, (curr_code, curr_code, curr_code), self.rect)

    def update_values(self, x, y, n):
        self.values[x * 3 + y] = n

    def get_location(self):
        return self.location[0] * self.cell_size, self.location[1] * self.cell_size

    def move_left(self):
        self.location[0] -= 1

    def move_right(self):
        self.location[0] += 1

    def move_top(self):
        self.location[1] -= 1

    def move_down(self):
        self.location[1] += 1


