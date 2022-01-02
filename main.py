# Import and initialize the pg library
import pygame as pg
from tic_tac_toe import TicTacToe
from tile import Tile

BLUE = (0,0,255)
GRAY = (192,192,192)
WHITE = (255,255,255)
PLAYER_VAL = 'O'
COMPUTER_VAL = 'X'

pg.init()

# Set up the drawing window
screen = pg.display.set_mode([600, 600])

# Fill the background with white
screen.fill(WHITE)

pg.display.set_caption("Tic-Tac-Toe")

tic_tac_toe = TicTacToe()

def draw_value_on_tile(tile):
    if tile.value == 'X':
        pg.draw.line(screen, BLUE, tile.pos, (tile.pos[0] + Tile.TILE_WIDTH, tile.pos[1] + Tile.TILE_HEIGHT))
        pg.draw.line(screen, BLUE, (tile.pos[0] + Tile.TILE_WIDTH, tile.pos[1]), (tile.pos[0], tile.pos[1] + Tile.TILE_HEIGHT))
        pg.display.update()
    else:
        pg.draw.circle(screen, BLUE, (tile.pos[0] + Tile.TILE_WIDTH // 2, tile.pos[1] + Tile.TILE_HEIGHT // 2), Tile.TILE_WIDTH // 2, 1)
        pg.display.update()
    pg.time.delay(300)


#draw grid
for i in range(TicTacToe.GRID_SIZE):
    for j in range(TicTacToe.GRID_SIZE):
        current_tile = tic_tac_toe.gameboard[i][j]
        pg.draw.rect(screen, GRAY, (current_tile.pos[0], current_tile.pos[1], Tile.TILE_WIDTH, Tile.TILE_HEIGHT))
        pg.draw.rect(screen, BLUE, (current_tile.pos[0], current_tile.pos[1], Tile.TILE_WIDTH, Tile.TILE_HEIGHT), 1)

# Run until the user asks to quit
found_winner = False
running = True
while running:
    pg.mouse.set_cursor(pg.cursors.diamond)

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    if pg.mouse.get_pressed() == (1,0,0):
        curr_tile = tic_tac_toe.player_place_val(pos)
        if curr_tile is not None:
            pg.display.set_caption("Tic-Tac-Toe")
            draw_value_on_tile(curr_tile)
        else:
            print("Tile was already pressed!")
            pg.display.set_caption("Can't place value there because this tile has already been pressed")


        if tic_tac_toe.check_winner(PLAYER_VAL):
            pg.display.set_caption("You tied!")

        computer_tile = tic_tac_toe.computer_place_val()
        if computer_tile is not None:
            draw_value_on_tile(computer_tile)
        else:
            pg.display.set_caption("You won!")

        if tic_tac_toe.check_winner(COMPUTER_VAL):
            pg.display.set_caption("You lost!")

        pg.time.delay(100)

    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
