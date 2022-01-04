from tile import Tile
import copy

class TicTacToe:
    GRID_SIZE = 3
    def __init__(self):
        self.gameboard = [[Tile((0,0)), Tile((200, 0)), Tile((400, 0))],[Tile((0, 200)), Tile((200, 200)), Tile((400, 200))],[Tile((0, 400)), Tile((200, 400)), Tile((400,400))]]

    def __str__(self):
        game_str = ""
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                game_str += str(self.gameboard[i][j])
                game_str += "\n"
        return game_str

    def check_winner(self, board, player_val):
        check_diagonal_right = True
        check_diagonal_left = True
        for i in range(TicTacToe.GRID_SIZE):
            if all([player_val == board[i][j].value for j in range(TicTacToe.GRID_SIZE)]): #check for if player has equal value in all entries in row
                return True
            if all([player_val == board[k][i].value for k in range(TicTacToe.GRID_SIZE)]): #check for if player has equal value in all entries in col
                return True
            if board[i][i].value != player_val:
                check_diagonal_right = False
            if board[i][TicTacToe.GRID_SIZE - (i + 1)].value != player_val:
                check_diagonal_left = False

        return check_diagonal_left or check_diagonal_right


    def check_for_filled_board(self, board):
        filled = True
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                if board[i][j].value == 'A':
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

    def yield_next_avail_spot(self, board):
        for i in range(TicTacToe.GRID_SIZE):
            for j in range(TicTacToe.GRID_SIZE):
                if not board[i][j].pressed:
                    yield (i, j)


    def game_over(self, board):
        return self.check_winner(board, 'X') or self.check_winner(board, 'O') or self.check_for_filled_board(board)

    def ai_place_val(self):
        max_score = float('-inf')
        best_move = (-1,-1)
        avail_tile = self.yield_next_avail_spot(self.gameboard)

        for coord in avail_tile:
            self.gameboard[coord[0]][coord[1]].press('X')
            curr_score = self.minimax(copy.deepcopy(self.gameboard), depth=0, is_maximized=False)
            if curr_score > max_score:
                max_score = curr_score
                best_move = (coord[0], coord[1])
            self.gameboard[coord[0]][coord[1]].unpress()

        if best_move != (-1,-1):
            self.gameboard[best_move[0]][best_move[1]].press('X')
            return self.gameboard[best_move[0]][best_move[1]]
        else:
            return None


    def minimax(self, board, depth, is_maximized):
        avail_tile = self.yield_next_avail_spot(board)
        if self.game_over(board):
            if self.check_winner(board, 'X'):
                return 1
            elif self.check_winner(board, 'O'):
                return -1
            else:
                return 0

        elif is_maximized:
            best_val = float('-inf')
            for coord in avail_tile:
                board[coord[0]][coord[1]].press('X')
                score = self.minimax(board, depth + 1, False)
                best_val = max(score, best_val)
                board[coord[0]][coord[1]].unpress()
            return best_val

        else:
            best_val = float('inf')
            for coord in avail_tile:
                board[coord[0]][coord[1]].press('O')
                score = self.minimax(board, depth + 1, True)
                best_val = min(score, best_val)
                board[coord[0]][coord[1]].unpress()
            return best_val
