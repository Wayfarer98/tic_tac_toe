import pygame as pg
import sys
import time
from pygame.locals import *
from check import check_filled, check_occupied, check_win
import numpy as np

symbs = {1: 'X', 2: 'O'}
board = np.full((3, 3), ' ')
turn = np.random.randint(1, 3)
symb = symbs[turn]

winner = None
draw = False

width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

initializing_window = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
o_img = pg.image.load("o_modified.png")

initializing_window = pg.transform.scale(initializing_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))

def game_initializing_window():
    screen.blit(initializing_window, (0, 0))

    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    global board, turn, symb, winner, draw

    if check_win(board, symb):
        winner = symb
        message = f"{symb} won!"
    elif check_filled(board):
        draw = True
        message = "Game is a draw!"
    else:
        message = f"{symb}'s turn!"

    switch_turn()

    font = pg.font.Font(None, 30)

    text = font.render(message, 1, white)

    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def switch_turn():
    global symb
    symb = 'O' if symb == 'X' else 'X'

def drawXO(row, col):  # sourcery skip: switch
    global board, symb, turn

    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30
    
    board[row-1, col-1] = symb

    if (symb == 'X'):
        screen.blit(x_img, (posy, posx))
    else:
        screen.blit(o_img, (posy, posx))
    pg.display.update()

def user_click():
    x, y = pg.mouse.get_pos()

    if x < width/3:
        col = 1
    elif x < width/3 * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None

    if y < height/3:
        row = 1
    elif y < height/3 * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None

    if row and col and board[row - 1, col - 1] == ' ':
        drawXO(row, col)

    draw_status()

def reset_game():
    global board, winner, symb, draw, symbs
    time.sleep(3)
    symb = symbs[np.random.randint(1, 3)]
    draw = False
    game_initializing_window()
    winner = None
    board = np.full((3, 3), ' ')

if __name__ == "__main__":
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                user_click()

                if winner or draw:
                    reset_game()

        pg.display.update()
        CLOCK.tick(fps)