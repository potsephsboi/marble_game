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

def marble_out_of_bounds():
    for m in Marble.FIRED:
        if not (0 < m.x < WIDTH and 0 < m.y < HEIGHT):
            Marble.MARBLES.remove(m)
            Marble.FIRED.remove(m)


def marble_collision():
    f = Marble.FIRED[0]
    for m in Marble.MARBLES:
        if m not in Marble.FIRED and m is not Marble.Player:
            m_dist = math.sqrt((m.x-f.x)**2 + (m.y-f.y)**2)
            if m_dist <= Marble.MARBLE_RADIUS*2:
                if f.color == m.color:
                    Marble.FIRED.remove(f)
                    Marble.MARBLES.remove(f)
                    Marble.MARBLES.remove(m)
                else:
                    f.y += m.y - f.y + 2 * Marble.MARBLE_RADIUS
                    f.x = m.x
                    Marble.FIRED.remove(f)
                return

               
