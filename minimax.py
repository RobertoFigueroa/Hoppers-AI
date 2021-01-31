def bestScore(hopper_board):
    bestScore = float('-inf')
    move = []
    for i in range(10):
        for j in range(10):
            if hopper_board[i][j] == '_':
                score = minimax(hopper_board,)
                


def minimax(board, depth, isMaximinzing):
    return 1

def findPath(board, boardsize, current_x, current_y, symbol):
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
    print("limitx----->", low_limit_x, up_limit_x)
    print("limity----->", low_limit_y, up_limit_y)

    for i in range(low_limit_x,up_limit_x):
        for j in range(low_limit_y, up_limit_y):
            if board[i][j] == '_':
                tiles_available.append((i+1,j+1))
    return tiles_available