import pygame 


WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw():
    WIN.fill(WHITE)
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

