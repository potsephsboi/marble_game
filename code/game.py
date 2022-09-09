from setup import *



def draw():
    WIN.fill(WHITE)
    WIN.blit(ARROW, (277, 380))   
    for m in Marble.MARBLES:
        m.drawMarble()
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()


if __name__ == '__main__':
    main()

