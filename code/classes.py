from setup import *

class Marble:
    Player = None 
    FIRED = []
    MARBLES = []
    MARBLE_RADIUS = 20
    def __init__(self, color, pos,  vx, vy, is_player) -> None:
        self.color = color 
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vx
        self.vy = vy
        self.pos = pos
        self.is_player = is_player
        if self.is_player:
            Marble.Player = self
        Marble.MARBLES.append(self)

    def __repr__(self) -> str:
        return f'{self.color} marble at ({self.x}, {self.y})'

    def drawMarble(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), Marble.MARBLE_RADIUS)
