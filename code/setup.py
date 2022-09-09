import pygame
import random

WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

COLORS = [BLACK, (124,252,0), (255,0,0), (24, 0, 255), (100, 0, 100)] 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

ARROW = pygame.image.load('../imgs/screen.png')
ARROW = pygame.transform.rotate(ARROW, -90)

from classes import Marble
for j in range(3):
    for i in range(int(WIDTH/(Marble.MARBLE_RADIUS*2))):
        Marble(COLORS[random.randint(0, len(COLORS)-1)], [i*(Marble.MARBLE_RADIUS)*2+Marble.MARBLE_RADIUS, j*(Marble.MARBLE_RADIUS)*2+Marble.MARBLE_RADIUS])
        
PLAYER = Marble(COLORS[random.randint(0, len(COLORS)-1)], [(WIDTH/2)-Marble.MARBLE_RADIUS/2, 500])   