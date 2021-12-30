# Import and initialize the pg library
import pygame as pg
from game_funcs import *
from random import randrange
from random import seed

PLAYER = 0
COMPUTER = 1

pg.init()

# Set up the drawing window
screen = pg.display.set_mode([500, 500])

# Fill the background with white
screen.fill((255, 255, 255))

pg.display.set_caption("Tic-Tac-Toe")

#set gameboard with diffult values
gameboard = [['a','b','c'], ['d','e','f'], ['g','h','i']]

#draw grid
pg.draw.line(screen, (0, 0, 255), (50,300), (450,300))
pg.draw.line(screen, (0, 0, 255), (50,150), (450,150))
pg.draw.line(screen, (0, 0, 255), (175,50), (175,450))
pg.draw.line(screen, (0, 0, 255), (325,50), (325,450))

# Run until the user asks to quit
running = True
while running:
    pg.mouse.set_cursor(pg.cursors.diamond)

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #player places a cirlcle
    pos = pg.mouse.get_pos()
    if pg.mouse.get_pressed() == (1,0,0):
        pg.draw.circle(screen, (0, 0, 255), pos, 25)
        update_gameboard(gameboard, pos, PLAYER)
        pg.time.delay(50)

        #computer places a square
        counter = 0
        rand_row = randrange(3)
        rand_col = randrange(3)
        while not check_coord(gameboard, (rand_row, rand_col)) and counter <= 9:
            rand_row = randrange(3)
            rand_col = randrange(3)
            counter += 1
        print("Computer coord", rand_row, rand_col)

        gameboard[rand_row][rand_col] = COMPUTER
        draw_at_grid_cord(screen, (rand_row, rand_col))

        player_win = check_winner(gameboard, PLAYER)
        computer_win = check_winner(gameboard, COMPUTER)

        winner = None
        if player_win:
            winner = PLAYER
        elif computer_win:
            winner = COMPUTER

        if winner is not None:
            print(f"The winner is {winner}")
            screen.fill((255, 255, 255))
            pg.time.delay(75)
            text_surface = pg.font.Font.render(pg.font.SysFont("arial", 30), f"The winner is {winner}", True, (0,0,255))
            pg.Surface.blit(screen, text_surface, (100,100))

        pg.time.delay(75)


    print(gameboard)
    if check_for_filled_board(gameboard):
        pg.quit()


    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
