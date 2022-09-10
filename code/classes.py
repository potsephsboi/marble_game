from setup import *

class Marble:
    MARBLES = []
    MARBLE_RADIUS = 20
    def __init__(self, color, pos) -> None:
        self.color = color 
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        Marble.MARBLES.append(self)

    def __repr__(self) -> str:
        return f'{self.color} marble at ({self.x}, {self.y})'

    def drawMarble(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), Marble.MARBLE_RADIUS)
