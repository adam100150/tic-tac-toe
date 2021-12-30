import pygame as pg

GRID_SIZE = 3

def check_winner(gameboard, player):
    for row in gameboard:
        if all([player == row[i] for i in range(GRID_SIZE)]): #check for if player has equal value in all rows
            return True
    for i in range(GRID_SIZE):
        col = [gameboard[j][i] for j in range(GRID_SIZE)]
        if all([player == col[k] for k in range(GRID_SIZE)]):
            return True

    check_diagonal = True
    for i in range(GRID_SIZE):
        if gameboard[i][i] != player:
            check_diagonal = False
    return check_diagonal

def update_gameboard(gameboard, pos, current_player):
    if pos[0] < 175 and pos[1] < 150: #top left box
        gameboard[0][0] = current_player
    elif 175 < pos[0] < 325 and pos[1] < 150: # middle left box
        gameboard[0][1] = current_player
    elif pos[0] > 325 and pos[1] < 150: #bottom left box
        gameboard[0][2] = current_player
    elif pos[0] < 175 and 150 < pos[1] < 300: #top middle box
        gameboard[1][0] = current_player
    elif 175 < pos[0] < 325 and 150 < pos[1] < 300: # middle centered box
         gameboard[1][1] = current_player
    elif pos[0] > 325 and 150 < pos[1] < 300: #bottom middle box
         gameboard[1][2] = current_player
    elif pos[0] < 175 and pos[1] > 300: #top right box
         gameboard[2][0] = current_player
    elif 175 < pos[0] < 325 and pos[1] > 300: #middle right box
         gameboard[2][1] = current_player
    elif pos[0] > 325 and pos[1] > 300: #bottom right box
         gameboard[2][2] = current_player
