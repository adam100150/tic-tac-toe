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

def draw_at_grid_cord(screen, cord):
    print("Drawing square")
    if cord == (0,0): #top left box
        pg.draw.rect(screen, (0,0,255), (75,75,50,50))
    elif cord == (1,0): # middle left box
        pg.draw.rect(screen, (0,0,255), (50,200,50,50))
    elif cord == (2,0): #bottom left box
        pg.draw.rect(screen, (0,0,255), (50,350,50,50))
    elif cord == (0,1): #top middle box
        pg.draw.rect(screen, (0,0,255), (225,50,50,50))
    elif cord == (1,1): # middle centered box
         pg.draw.rect(screen, (0,0,255), (225,200,50,50))
    elif cord == (2,1): #bottom middle box
         pg.draw.rect(screen, (0,0,255), (50,50,50,50))
    elif cord == (0,2): #top right box
         pg.draw.rect(screen, (0,0,255), (400,50,50,50))
    elif cord == (1,2): #middle right box
         pg.draw.rect(screen, (0,0,255), (400,225,50,50))
    elif cord == (2,2): #bottom right box
         pg.draw.rect(screen, (0,0,255), (375,350,50,50))

def check_coord(gameboard, cord):
    return isinstance(gameboard[cord[0]][cord[1]],str)

def check_for_filled_board(gameboard):
    filled = True
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if isinstance(gameboard[i][j],str):
                filled = False
    return filled
