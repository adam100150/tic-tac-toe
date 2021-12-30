# Import and initialize the pg library
import pygame as pg
from game_funcs import *


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

current_player = 0
counter = 0

# Run until the user asks to quit
running = True
while running:
    pg.mouse.set_cursor(pg.cursors.diamond)

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    if pg.mouse.get_pressed() == (1,0,0):
        if current_player == 0:
            pg.draw.circle(screen, (0, 0, 255), pos, 25)
            update_gameboard(gameboard, pos, current_player)
        else:
            pg.draw.rect(screen, (0, 0, 255), (pos[0], pos[1], 50, 50))
            update_gameboard(gameboard, pos, current_player)
        pg.time.delay(150)

        winner = check_winner(gameboard, current_player)
        if winner:
            print(f"The winner is player {current_player}")
            screen.fill((255, 255, 255))
            pg.time.delay(75)
            text_surface = pg.font.Font.render(pg.font.SysFont("arial", 30), f"The winner is player {current_player}", True, (0,0,255))
            pg.Surface.blit(screen, text_surface, (100,100))

        counter += 1
        current_player = counter % 2
        pg.time.delay(75)


    #print(gameboard)


    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
