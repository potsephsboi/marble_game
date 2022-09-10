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

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(pygame.mouse.get_pos())


if __name__ == '__main__':
    main()

