import time
from setup import *
from helper import *


def draw(mouse, show_level, levelid):
    WIN.fill(WHITE)   
    if show_level:
        level_txt = font.render(f'LEVEL {levelid}', True, BLACK, WHITE)
        txt_rect = level_txt.get_rect()
        txt_rect.center = (WIDTH / 2, HEIGHT / 2)
        WIN.blit(level_txt, txt_rect)
    

    for m in Marble.MARBLES:
        m.drawMarble()

    start_pos = ((WIDTH/2)-Marble.MARBLE_RADIUS/2, 500)
    end_pos = find_pos(mouse)
    if start_pos is not None and end_pos is not None:
        pygame.draw.line(WIN, BLACK, start_pos, end_pos, 5)
    pygame.draw.line(WIN, BLACK, (0, 360), (WIDTH, 360), 5)
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
    t0 = time.time()
    pause_time = 2
    pause = True
    cur_level = 1

    setup_game(cur_level)

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                if not pause and len(Marble.FIRED) < 5:
                    fire(pygame.mouse.get_pos())

        pause = time.time() - t0 <= pause_time

        move_marbles()
        if len(Marble.FIRED) > 0:
            marble_collision()

        marble_out_of_bounds()
        game_status = check_game_over()
        if game_status[0]:
            if game_status[1] == 1:
                cur_level += 1
                t0 = time.time()
                pause = True
                if cur_level > 3:
                    handle_win()
                    run = False
                setup_game(cur_level)

            if game_status[1] == 0 and not pause:
                print('You lost :(')
                run = False

        draw(pygame.mouse.get_pos(), pause, cur_level)


if __name__ == '__main__':
    main()

