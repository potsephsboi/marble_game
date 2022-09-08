from helper import *




def draw():
    WIN.fill(WHITE)
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

