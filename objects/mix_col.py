import pygame 
from time import sleep
from .key_col import KeyCol

class MixCol(KeyCol):

    def __init__(self, grid, value, x, y, size, speed):
        super().__init__(grid, value, x, y, size, speed)
        self.sub = self.col
        self.col.fill('#000000')

        self.font = pygame.font.Font('freesansbold.ttf', 25)
        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render("MIX", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)
        self.m_mat = [[2,3,1,1], [1,2,3,1], [1,1,2,3], [3,1,1,2]]
    def show_mix(self, val):

        sleep(0.5)

        ##think of how the animation will look
        #MIX col mul happens row wise

        

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render(str((val[0] * self.m_mat[i][0])%283), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render("^", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render(str((val[1] * self.m_mat[i][1])), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render("^", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render(str((val[2] * self.m_mat[i][2])), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render("^", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render(str((val[3] * self.m_mat[i][3])), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render("=", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render(str((((val[0] * self.m_mat[i][0]))^((val[1] * self.m_mat[i][1]))^((val[2] * self.m_mat[i][2])) ^ ((val[3] * self.m_mat[i][3])))%283 ), True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)
        
        sleep(0.8)

        sleep(0.8)

        for i in range(4):
            rect = pygame.Rect(0, i * self.size, self.size, self.size)
            pygame.draw.rect(self.col, (176, 104, 247), rect)
            number = self.font.render("MIX", True, (255, 255, 255), None)
            rect1 = number.get_rect()
            rect1.center = [0.5 * self.size, (i+0.5) * self.size]
            self.col.blit(number, rect1)

        



        



        #print([((val[0] * self.m_mat[i][0])%283)^((val[1] * self.m_mat[i][1])%283)^((val[2] * self.m_mat[i][2])%283) ^ ((val[3] * self.m_mat[i][3])%283)  for i in range(4)])

        


        return [((val[0] * self.m_mat[i][0])%283)^((val[1] * self.m_mat[i][1])%283)^((val[2] * self.m_mat[i][2])%283) ^ ((val[3] * self.m_mat[i][3])%283)  for i in range(4)]