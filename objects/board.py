import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.size = size
        self.board = pygame.Surface([8 * self.size, 2 * self.size])
        self.board.fill('#000000')
        self.location = [x * self.size, y * self.size]
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.text = "--------------------"
        self.set_text(self.text)

    def get_location(self):
        return self.location[0], self.location[1]

    def set_text(self, text):
        self.text = text
        rect = pygame.Rect(0, 0, 8 * self.size, 2 * self.size)
        pygame.draw.rect(self.board, (191, 121, 247), rect)
        number = self.font.render(text, True, (255, 255, 255), None)
        rect1 = number.get_rect()
        rect1.center = [4 * self.size, self.size]
        self.board.blit(number, rect1)

    def set_2_line_text(self, text):
        rect = pygame.Rect(0, 0, 8 * self.size, 2 * self.size)
        pygame.draw.rect(self.board, (191, 121, 247), rect)
        number = self.font.render(text[0], True, (255, 255, 255), None)
        rect1 = number.get_rect()
        rect1.center = [4 * self.size, self.size * 0.7]
        self.board.blit(number, rect1)
        number = self.font.render(text[1], True, (255, 255, 255), None)
        rect1 = number.get_rect()
        rect1.center = [4 * self.size, self.size * 1.4]
        self.board.blit(number, rect1)
