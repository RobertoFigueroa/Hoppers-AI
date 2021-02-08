#aqui es donde se generan los nodos de la siguiente forma
#se genera un tablero cuando un hay un espacio inmediato
#vacio y cuando hay una casilla ocupada y se puede hacer
#un salto
#el heuristco se puede definir en función de lo que avance
from math import sqrt,log

LADDER_COORDS = [(2,4),(3,3),(4,2)]
LADDER_POSITIONS = [(n[0]+i,n[1]+i) for i in range(0,4) for n in LADDER_COORDS]

def bestScore(hopper):
    coins = hopper.coins_position()
    bestScore = float('-inf')
    best_position = None
    #check for all posibles moves and minimax each one in order to find the best score
    for i in coins:
        path = findPath(hopper.board,10, i[0], i[1],'O', False) #O can be change by a global variable
        if len(path) > 0:
            for coord in path:
                hopper.board[coord[0]-1][coord[1]-1] = 'O' #again this could be a global variable
                hopper.board[i[0]][i[1]] = '_'
                score = minimax(hopper, 2,float('-inf'), float('inf'), True)
                hopper.board[i[0]][i[1]] = 'O'
                hopper.board[coord[0]-1][coord[1]-1] = '_' #again this could be a global variable
                
                #hopper_board[coord[0]][coord[1]] = '_' #reverting to initial state
                if score > bestScore:
                    bestScore = score
                    best_position = [i[0]+1, i[1]+1, coord[0], coord[1]]
    return best_position

def minimax(game, depth, alpha, beta, isMaximinzing):
    winner = game.check_for_winner()
    if depth == 0 or winner != 0:
        p = distance_heuristic(game, isMaximinzing)
       # print(game.print_board())
        return p
    
    if isMaximinzing:
        bestScore = float('-inf')
        coins = game.coins_position(isAI=False)
        for i in coins:
            path = findPath(game.board, 10, i[0], i[1], 'X',False)
            if len(path) > 0:
                for coord in path:
                    game.board[coord[0]-1][coord[1]-1] = 'X'
                    game.board[i[0]][i[1]] = '_'
                    score = minimax(game, depth-1, alpha, beta, False)
                    game.board[i[0]][i[1]] = 'X'
                    game.board[coord[0]-1][coord[1]-1] = '_'
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestScore
    else:
        bestScore = float('inf')
        coins = game.coins_position()
        for i in coins:
            path = findPath(game.board, 10, i[0], i[1], 'O',False)
            if len(path) > 0:
                for coord in path:
                    game.board[coord[0]-1][coord[1]-1] = 'O'
                    game.board[i[0]][i[1]] = 'O'
                    score = minimax(game, depth-1, alpha, beta, True)
                    game.board[i[0]][i[1]] = 'O'
                    game.board[coord[0]-1][coord[1]-1] = '_'
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestScore


    # if depth == 0 or winner:
    #     return 1 #heuristic value of the node
    # if isMaximinzing:
    #     #for path in findPath(git ) 
    # return 
    

        

#current_x and current_y has to be in board notation (0-9)
def findPath(board, boardsize, current_x, current_y, symbol, isJumping): #refactor to find_possiblilities or something like that
    tiles_available = []
    low_limit_x = current_x -1
    up_limit_x = current_x + 2
    low_limit_y = current_y -1
    up_limit_y = current_y +2
    if low_limit_x < 0:
        low_limit_x = current_x
    if up_limit_x > 10:
        up_limit_x = current_x +1
    if low_limit_y < 0:
        low_limit_y = current_y
    if up_limit_y > 10:
        up_limit_y = current_y + 1
   
    if isJumping:   
        av_tiles = []
        for i in range(low_limit_x, up_limit_x):
            for j in range(low_limit_y, up_limit_y):
                if board[i][j] != '_':
                    jump_x = 2*i-current_x
                    jump_y = 2*j-current_y
                    if jump_x >= 0 and jump_x <10 and jump_y >= 0 and jump_y < 10: #just to be sure and not get an error
                        if board[jump_x][jump_y] == '_':
                            av_tiles.append((jump_x+1, jump_y+1))
                            board[jump_x][jump_y] = 'X' 
                            paths = findPath(board, 10, jump_x, jump_y,'X', True)
                            board[jump_x][jump_y] = '_' 
                            av_tiles = av_tiles + paths
        return av_tiles

    else:
        av_tiles = []
        for i in range(low_limit_x,up_limit_x):
            for j in range(low_limit_y, up_limit_y):
                if board[i][j] == '_':
                    av_tiles.append((i+1,j+1))
                else:
                    jump_x = 2*i-current_x
                    jump_y = 2*j-current_y
                    if jump_x >= 0 and jump_x <10 and jump_y >= 0 and jump_y < 10: #just to be sure and not get an error
                        if board[jump_x][jump_y] == '_':
                            board[jump_x][jump_y] = 'X' 
                            paths = findPath(board, 10, jump_x, jump_y,'X', True)
                            board[jump_x][jump_y] = '_' 
                            av_tiles.append((jump_x+1,jump_y+1))
                            av_tiles = av_tiles+paths
        return av_tiles
    

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


def distance_heuristic(game, isMaximizing):
    points = 0
    coins = game.coins_position(isMaximizing)
    for i in coins:
        if i in LADDER_POSITIONS:
            points += 1
    if isMaximizing: #this is for add more points when is closer to goal
        closer_coin = min(coins)
        distance = sqrt((0-closer_coin[0])**2+(0-closer_coin[1])**2)
        points += -log(distance+1,10)+3
    else:
        closer_coin = max(coins)
        distance = sqrt((9-closer_coin[0])**2+(9-closer_coin[1])**2)
        points += -log(distance+1,10)+3
        
    return points

        