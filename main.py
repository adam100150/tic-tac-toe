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
        player_tile = tic_tac_toe.player_place_val(pos)
        if player_tile is not None:
            pg.display.set_caption("Tic-Tac-Toe")
            placed_in_filled_spot = False
            draw_value_on_tile(player_tile)
        else:
            print("Tile was already pressed!")
            pg.display.set_caption("Can't place value there because this tile has already been pressed")
            placed_in_filled_spot = True

        if not found_winner and not placed_in_filled_spot:
            if tic_tac_toe.check_winner(tic_tac_toe.gameboard, PLAYER_VAL):
                pg.display.set_caption("You won!")
                found_winner = True

            computer_tile = tic_tac_toe.ai_place_val()
            if computer_tile is None: #couldn't place a value which means the board is full
                pg.display.set_caption("You tied!")
                found_winner = True
            else:
                draw_value_on_tile(computer_tile)

            if tic_tac_toe.check_winner(tic_tac_toe.gameboard, COMPUTER_VAL):
                pg.display.set_caption("You lost!")
                found_winner = True

        pg.time.delay(100)

    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
