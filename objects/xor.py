import pygame
from time import sleep
from .key_col import KeyCol


class Xor(KeyCol):

    def __init__(self, grid, value, x, y, size, speed):
        super().__init__(grid, value, x, y, size, speed)
        self.col.fill('#000000')
        self.val = ['XOR', 'XOR', 'XOR', 'XOR']
        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render(self.val[i], True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        self.font = pygame.font.Font('freesansbold.ttf', 25)

    def show_xor(self, val1, val2):
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
            number = self.font.render("^", True, (255, 255, 255), None)
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

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render("=", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (0, 0, 0), rect)
            number = self.font.render(str(val1[i] ^ val2[i]), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        return [val1[i] ^ val2[i] for i in range(4)]
