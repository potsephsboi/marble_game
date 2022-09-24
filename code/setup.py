import pygame
import random

WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (124,252,0)
RED = (255, 0, 0)
BLUE = (24, 0, 255)
PURPLE = (100, 0, 100)
COLORS = [BLACK, GREEN, RED, BLUE, PURPLE] 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.init()
pygame.display.set_caption('SHOOT DEM MARBLES')

font = pygame.font.Font('freesansbold.ttf', 32)


ARROW_LEN = 80


from classes import Marble
def setup_game(level):
    Marble.MARBLES.clear()  
    Marble.FIRED.clear()
    Marble.Player = None
    Marble(COLORS[random.randint(0, len(COLORS)-1)], [(WIDTH/2)-Marble.MARBLE_RADIUS/2, 500], 0, 0, True)
    for j in range(level):
        for i in range(1):
                Marble(COLORS[random.randint(0, len(COLORS)-1)], [i*(Marble.MARBLE_RADIUS)*2+Marble.MARBLE_RADIUS, j*(Marble.MARBLE_RADIUS)*2+Marble.MARBLE_RADIUS], 0, 0, False)

# int(WIDTH/(Marble.MARBLE_RADIUS*2))