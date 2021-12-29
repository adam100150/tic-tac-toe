# Import and initialize the pg library
import pygame as pg


pg.init()

# Set up the drawing window
screen = pg.display.set_mode([500, 500])

# Fill the background with white
screen.fill((255, 255, 255))

pg.display.set_caption("Tic-Tac-Toe")

#set gameboard with diffult values
gameboard = [['a','b','c'], ['d','e','f'], ['g','h','i']]

# Draw the grid
pg.draw.line(screen, (0, 0, 255), (50,300), (450,300))
pg.draw.line(screen, (0, 0, 255), (50,150), (450,150))
pg.draw.line(screen, (0, 0, 255), (175,50), (175,450))
pg.draw.line(screen, (0, 0, 255), (325,50), (325,450))

current_player = 0
counter = 0

def update_gameboard(pos):
    if pos[0] < 175 and pos[1] < 150: #top left corner
        gameboard[0][0] = current_player
    elif 175 < pos[0] < 325 and pos[1] < 150:
        gameboard[0][1] = current_player
    elif pos[0] > 325 and pos[1] < 150:
        gameboard[0][2] = current_player
    elif pos[0] < 175 and 150 < pos[1] < 300:
        gameboard[1][0] = current_player
    elif 175 < pos[0] < 325 and 150 < pos[1] < 300:
         gameboard[1][1] = current_player
    elif pos[0] > 325 and 150 < pos[1] < 300:
         gameboard[1][2] = current_player
    elif pos[0] < 175 and pos[1] > 300:
         gameboard[2][0] = current_player
    elif 175 < pos[0] < 325 and pos[1] > 300:
         gameboard[2][1] = current_player
    elif pos[0] > 325 and pos[1] > 300:
         gameboard[2][2] = current_player

def check_winner():
    for i in range(3):
        if gameboard[i][0] == gameboard[i][1] and gameboard[i][1] == gameboard[i][2]: #check for equal rows
            return gameboard[i][0]
        if gameboard[0][i] == gameboard[1][i] and gameboard[1][i] == gameboard[2][i]: #check for equal columns
            return gameboard[0][i]
    if gameboard[0][0] == gameboard[1][1] and gameboard[1][1] == gameboard[2][2]: #check for diagonal
        return gameboard[0][0]
    if gameboard[0][2] == gameboard[1][1] and gameboard[1][1] == gameboard[2][0]: #check for other diagonal
        return gameboard[0][2]


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
            update_gameboard(pos)
        else:
            pg.draw.rect(screen, (0, 0, 255), (pos[0], pos[1], 50, 50))
            update_gameboard(pos)

        winner = check_winner()
        if winner is not None:
            print(f"The winner is player{winner}")
            screen.fill((255, 255, 255))
            pg.time.delay(75)
            text_surface = pg.font.Font.render(pg.font.SysFont("arial", 30), f"The winner is player{winner}", True, (0,0,255))
            pg.Surface.blit(screen, text_surface, (100,100))

        counter += 1
        current_player = counter % 2
        pg.time.delay(75)


    print(gameboard)


    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
