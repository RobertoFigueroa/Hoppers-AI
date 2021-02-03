#aqui es donde se generan los nodos de la siguiente forma
#se genera un tablero cuando un hay un espacio inmediato
#vacio y cuando hay una casilla ocupada y se puede hacer
#un salto
#el heuristco se puede definir en función de lo que avance
from math import sqrt

def bestScore(hopper):
    hopper_board = hopper.board
    coins = hopper.coins_position()
    bestScore = float('-inf')
    best_position = None
    #check for all posibles moves and minimax each one in order to find the best score
    for i in coins:
        path = findPath(hopper_board,10, i[0], i[1],'O') #O can be change by a global variable
        if len(path) > 0:
            for coord in path:
                child_board = hopper_board
                child_board[coord[0]-1][coord[1]-1] = 'O' #again this could be a global variable
                score = minimax(child_board, 3, True)
                child_board[coord[0]-1][coord[1]-1] = '_' #again this could be a global variable
                
                #hopper_board[coord[0]][coord[1]] = '_' #reverting to initial state
                if (score > bestScore):
                    bestScore = score
                    best_position = [i[0]+1, i[1]+1, coord[0], coord[1]]
    return best_position

def minimax(board, depth, isMaximinzing):
    # winner = False #check for winner

    # if depth == 0 or winner:
    #     return 1 #heuristic value of the node
    # if isMaximinzing:
    #     #for path in findPath(git ) 
    # return 
    
    return 1

        


def findPath(board, boardsize, current_x, current_y, symbol): #refactor to find_possiblilities or something like that
    tiles_available = []
    low_limit_x = current_x -1
    up_limit_x = current_x + 2
    low_limit_y = current_y -1
    up_limit_y = current_y +2
    if low_limit_x < 0:
        low_limit_x = current_x
    if up_limit_x >= 10:
        up_limit_x = current_x +1
    if low_limit_y < 0:
        low_limit_y = current_y
    if up_limit_y >= 10:
        up_limit_y = current_y + 1
    for i in range(low_limit_x,up_limit_x):
        for j in range(low_limit_y, up_limit_y):
            if board[i][j] == '_':
                tiles_available.append((i+1,j+1))
            # else:
            #     distance = sqrt((current_x-i)**2+(current_y-j)**2)
            #     if distance > 1:
            #         new_pos_x, new_pox_y

    return tiles_available

        