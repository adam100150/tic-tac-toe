from tile import Tile

class TicTacToe:
    GRID_SIZE = 3
    def __init__(self):
        self.gameboard = [[Tile((0,0)), Tile((200, 0)), Tile((400, 0))],[Tile((0, 200)), Tile((200, 200)), Tile((400, 200))],[Tile((0, 400)), Tile((200, 400)), Tile((400,400))]]
        self.dist = self.row_and_col_vals()

    def __str__(self):
        game_str = ""
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                game_str += str(self.gameboard[i][j])
                game_str += "\n"
        return game_str

    def check_winner(self, player_val):
        check_diagonal_right = True
        check_diagonal_left = True
        for i in range(TicTacToe.GRID_SIZE):
            if all([player_val == self.gameboard[i][j].value for j in range(TicTacToe.GRID_SIZE)]): #check for if player has equal value in all entries in row
                return True
            if all([player_val == self.gameboard[k][i].value for k in range(TicTacToe.GRID_SIZE)]): #check for if player has equal value in all entries in col
                return True
            if self.gameboard[i][i].value != player_val:
                check_diagonal_right = False
            if self.gameboard[i][TicTacToe.GRID_SIZE - (i + 1)].value != player_val:
                check_diagonal_left = False

        return check_diagonal_left or check_diagonal_right


    def check_for_filled_board(self):
        filled = True
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                if isinstance(gameboard[i][j],str):
                    filled = False
        return filled

    #press a tile. If the tile already has a value in it, return None
    def player_place_val(self, pos):
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                current_tile = self.gameboard[i][j]
                #check which tile the curser pressed
                if current_tile.pos[0] < pos[0] < current_tile.pos[0] + current_tile.TILE_WIDTH and current_tile.pos[1] < pos[1] < current_tile.pos[1] + current_tile.TILE_HEIGHT:
                    if current_tile.pressed:
                        return None
                    else:
                        current_tile.value = 'O'
                        current_tile.pressed = True
                        return current_tile

    def computer_place_val(self):
        found_coord = False
        for coord in self.dist:
            if not self.gameboard[coord[0]][coord[1]].pressed:
                row = coord[0]
                col = coord[1]
                found_coord = True
                break

        if not found_coord:
            return None
        else:
            self.gameboard[row][col].value = 'X'
            return self.gameboard[row][col]

    def row_and_col_vals(self):
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                yield (i,j)

    def print_list_tile(self, lst):
        for i in lst:
            print(i)
