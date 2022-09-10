import math
from setup import *

def find_pos(mouse):
    global ARROW_LEN

    ax = Marble.MARBLES[0].x
    ay = Marble.MARBLES[0].y
    dy = mouse[1] - ay
    dx = mouse[0] - ax
    print(dx, dy)
    if dy != 0:
        angle = math.atan(dx/dy)
        # print(math.degrees(angle))
        return (ax+ARROW_LEN*math.sin(angle), ay+ARROW_LEN*math.cos(angle))


