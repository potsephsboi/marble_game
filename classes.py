from helper import *

class Marble:
    marbles = []
    def __init__(self, color, pos) -> None:
        self.color = color 
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        Marble.marbles.append(self)

    def __repr__(self) -> str:
        return f'{self.color} marble at ({self.x}, {self.y})'

    def drawMarble(self):
        pygame.draw.circle(WIN, BLACK, self.pos, 5)
