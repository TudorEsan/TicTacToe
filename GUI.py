import pygame
from minimax import best_move, get_moves, get_state
from time import sleep
from threading import Thread
win = None
screen_width = 600
square_width = 200
BLACK = (0, 0, 0)
grid = [['-' for _ in range(3)] for _ in range(3)]


def reset_grid():
    global win, screen_width, square_width, BLACK, grid
    win.fill((255, 255, 255))
    for i in range(0, screen_width, square_width):
        for j in range(0, screen_width, square_width):
            pygame.draw.rect(win, BLACK, (i, j, square_width, square_width), width=1)
    grid = [['-' for _ in range(3)] for _ in range(3)]


def get_index(x):
    global square_width
    return x // square_width


def draw_o(x, y):
    global win, BLACK
    pygame.draw.circle(win, BLACK, (x + square_width // 2, y + square_width // 2), square_width // 2 - 10, width=7)


def draw_x(x, y):
    global win, BLACK
    pygame.draw.line(win, BLACK, (x + 20, y + 20), (x + square_width - 20, y + square_width - 20), 10)
    pygame.draw.line(win, BLACK, (x + square_width - 20, y + 20), (x + 20, y + square_width - 20), 10)


def x_move(event):
    x, y = event.pos
    x -= x % square_width
    y -= y % square_width
    if grid[get_index(y)][get_index(x)] == '-':
        grid[get_index(y)][get_index(x)] = 'x'
        draw_x(x, y)
        try:
            if len(get_moves(grid)) != 9:
                o_move()
        except TypeError:
            sleep_reset()


def o_move():
    global grid
    move = best_move(grid)
    if move is not None:
        grid[move[0]][move[1]] = 'o'
        draw_o(move[1] * square_width, move[0] * square_width)
        check_winner(grid)


def sleep_reset():
    def f():
        pygame.display.update()
        sleep(1.5)
        reset_grid()

    t = Thread(target=f)
    t.start()
    t.join()


def check_winner(b):
    global win, square_width, screen_width

    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2]:
            if b[i][0] == 'x':
                pygame.draw.line(win, (255, 0, 0), (20, i * square_width + square_width // 2),
                                 (screen_width - 20, i * square_width + square_width // 2), width=7)
                sleep_reset()
                break
            if b[i][0] == 'o':
                pygame.draw.line(win, (255, 0, 0), (20, i * square_width + square_width // 2),
                                 (screen_width - 20, i * square_width + square_width // 2), width=7)
                sleep_reset()
                break
        if b[0][i] == b[1][i] == b[2][i]:
            if b[0][i] == 'x':
                pygame.draw.line(win, (255, 0, 0), (i * square_width + square_width // 2, 20),
                                 (i * square_width + square_width // 2, screen_width - 20), width=7)
                sleep_reset()
                break
            if b[0][i] == 'o':
                pygame.draw.line(win, (255, 0, 0), (i * square_width + square_width // 2, 20),
                                 (i * square_width + square_width // 2, screen_width - 20), width=7)
                sleep_reset()
                break
    if b[0][0] == b[1][1] == b[2][2]:
        if b[0][0] == 'o':
            pygame.draw.line(win, (255, 0, 0), (20, 20), (screen_width - 20, screen_width - 20), width=7)
            sleep_reset()
        if b[0][0] == 'x':
            pygame.draw.line(win, (255, 0, 0), (20, 20), (screen_width - 20, screen_width - 20), width=7)
            sleep_reset()
    if b[2][0] == b[1][1] == b[0][2]:
        if b[2][0] == 'o':
            pygame.draw.line(win, (255, 0, 0), (screen_width - 20, 20), (20, screen_width - 20), width=7)
            sleep_reset()
        if b[2][0] == 'x':
            pygame.draw.line(win, (255, 0, 0), (screen_width - 20, 20), (20, screen_width - 20), width=7)
            sleep_reset()
    if get_moves(grid) is None:
        sleep_reset()


def main():
    global screen_width, win, grid
    win = pygame.display.set_mode((screen_width, screen_width))
    win.fill((255, 255, 255))
    running = True
    reset_grid()
    while running:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_move(event)

        pygame.display.update()
    pygame.quit()


main()
