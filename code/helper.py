import math
from setup import *

def find_pos(mouse):
    global ARROW_LEN

    ax = Marble.Player.x    
    ay = Marble.Player.y    
    dy = mouse[1] - ay
    dx = mouse[0] - ax
    if dy > 0:
        angle = math.atan(dx/dy)
        return (ax+ARROW_LEN*math.sin(angle), ay+ARROW_LEN*math.cos(angle))
    elif dy < 0:
        angle = math.atan(dx/dy)
        return (ax-ARROW_LEN*math.sin(angle), ay-ARROW_LEN*math.cos(angle))

def move_marbles():
    for m in Marble.FIRED:
        m.x += m.vx
        m.y += m.vy

def calc_velocity(mouse, mx, my):
    vx = (mouse[0] - mx) // 10
    vy = (mouse[1] - my) // 10

    return [vx, vy]
