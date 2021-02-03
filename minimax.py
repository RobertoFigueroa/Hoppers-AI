#aqui es donde se generan los nodos de la siguiente forma
#se genera un tablero cuando un hay un espacio inmediato
#vacio y cuando hay una casilla ocupada y se puede hacer
#un salto
#el heuristco se puede definir en función de lo que avance
from math import sqrt

def bestScore(hopper):
    coins = hopper.coins_position()
    bestScore = float('-inf')
    best_position = None
    #check for all posibles moves and minimax each one in order to find the best score
    for i in coins:
        path = findPath(hopper.board,10, i[0], i[1],'O') #O can be change by a global variable
        if len(path) > 0:
            for coord in path:
                hopper.board[coord[0]-1][coord[1]-1] = 'O' #again this could be a global variable
                score = minimax(hopper, 3, True)
                hopper.board[coord[0]-1][coord[1]-1] = '_' #again this could be a global variable
                
                #hopper_board[coord[0]][coord[1]] = '_' #reverting to initial state
                if score > bestScore:
                    bestScore = score
                    best_position = [i[0]+1, i[1]+1, coord[0], coord[1]]
    return best_position

def minimax(game, depth, isMaximinzing):
    winner = game.check_for_winner()
    if depth == 0 or winner != 0:
        return 1 #it should be heuristic_fucntion
    
    if isMaximinzing:
        bestScore = float('-inf')
        coins = game.coins_position(isAI=False)
        for i in coins:
            path = findPath(game.board, 10, i[0], i[1], 'X')
            if len(path) > 0:
                for coord in path:
                    game.board[coord[0]-1][coord[1]-1] = 'X'
                    score = minimax(game, depth-1, False)
                    game.board[coord[0]-1][coord[1]-1] = '_'
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        coins = game.coins_position(isAI=False)
        for i in coins:
            path = findPath(game.board, 10, i[0], i[1], 'X')
            if len(path) > 0:
                for coord in path:
                    game.board[coord[0]-1][coord[1]-1] = 'X'
                    score = minimax(game, depth-1, True)
                    game.board[coord[0]-1][coord[1]-1] = '_'
                    bestScore = min(score, bestScore)
        return bestScore


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

    


def check_for_winner(board):
    first_player_columns = 5
    first_player_coins = 0
    second_player_coins = 0
    free_space_coins = 0
    for i in range(5):
        for j in range(first_player_columns):
            if board[i][j] == 'X':
                first_player_coins += 1
            if board[i][j] == '_':
                free_space_coins += 1
        first_player_columns -= 1
    
    if first_player_coins < 15 and free_space_coins == 0:
        return 1 #1 Means first player won

    free_space_coins = 0   
    second_player_columns = 9
    for i in range(5,10):
        for j in range(second_player_columns,10):
            if board[i][j] == 'O':
                second_player_coins += 1
            if board[i][j] == '_':
                free_space_coins += 1
        second_player_columns -= 1

    if second_player_coins < 15 and free_space_coins == 0:
        return -1 #means second player won
    
    return 0 #no winner
