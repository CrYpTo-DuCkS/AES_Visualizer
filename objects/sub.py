import pygame
from time import sleep
from .key_col import KeyCol


class Sub(KeyCol):
    def __init__(self, grid, value, x, y, size, speed):
        super().__init__(grid, value, x, y, size, speed)
        self.sub = self.col
        self.col.fill('#000000')

        self.font = pygame.font.Font('freesansbold.ttf', 25)
        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render("SUB", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        # number = self.font.render('>', True, (255, 255, 255), None)
        # rect1 = number.get_rect()
        # rect1.center = [0.5 * self.size, 0.5 * self.size]
        # self.col.blit(number, rect1)
        #
        # number = self.font.render('>', True, (255, 255, 255), None)
        # rect2 = number.get_rect()
        # rect2.center = [0.5 * self.size, 1.5 * self.size]
        # self.col.blit(number, rect2)
        #
        # number = self.font.render('>', True, (255, 255, 255), None)
        # rect3 = number.get_rect()
        # rect3.center = [0.5 * self.size, 2.5 * self.size]
        # self.col.blit(number, rect3)
        #
        # self.font = pygame.font.Font('freesansbold.ttf', 20)
        # number = self.font.render('SUB', True, (255, 255, 255), None)
        # rect4 = number.get_rect()
        # rect4.center = [0.5 * self.size, 3.5 * self.size]
        # self.col.blit(number, rect4)

    def show_sub(self, val1, val2):
        sleep(0.5)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render(str(val2[i]), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render(">>", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render(str(val1[i]), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)


