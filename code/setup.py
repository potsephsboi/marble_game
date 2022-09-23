import pygame
import random

WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

COLORS = [BLACK, (124,252,0), (255,0,0), (24, 0, 255), (100, 0, 100)] 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.display.set_caption('SHOOT DEM MARBLES')

ARROW_LEN = 80

from classes import Marble

Marble(COLORS[random.randint(0, len(COLORS)-1)], [(WIDTH/2)-Marble.MARBLE_RADIUS/2, 500], 0, 0, True)
for j in range(3):
    for i in range(int(WIDTH/(Marble.MARBLE_RADIUS*2))):
        Marble(COLORS[random.randint(0, len(COLORS)-1)], [i*(Marble.MARBLE_RADIUS)*2+Marble.MARBLE_RADIUS, j*(Marble.MARBLE_RADIUS)*2+Marble.MARBLE_RADIUS], 0, 0, False)
        