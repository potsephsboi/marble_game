from setup import *
from helper import *


def draw(mouse):
    WIN.fill(WHITE)   
    
    for m in Marble.MARBLES:
        m.drawMarble()

    start_pos = ((WIDTH/2)-Marble.MARBLE_RADIUS/2, 500)
    end_pos = find_pos(mouse)
    if start_pos is not None and end_pos is not None:
        pygame.draw.line(WIN, BLACK, start_pos, end_pos, 5)

    pygame.display.update()

def fire(mouse):
    vx = (mouse[0] - Marble.Player.x) / 10 
    vy = (mouse[1] - Marble.Player.y) / 10 
    Marble.Player.vx, Marble.Player.vy, = vx, vy         
    Marble.FIRED.append(Marble.Player)    

    Marble.Player = None
    Marble(COLORS[random.randint(0, len(COLORS)-1)], [(WIDTH/2)-Marble.MARBLE_RADIUS/2, 500], 0, 0, True)

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                if len(Marble.FIRED) < 5:
                    fire(pygame.mouse.get_pos())

        move_marbles()
        if len(Marble.FIRED) > 0:
            marble_collision()
        marble_out_of_bounds()
        draw(pygame.mouse.get_pos())


if __name__ == '__main__':
    main()

