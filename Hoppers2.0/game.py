from types import coroutine
from board import Board
from minimax import Minimax
from node import Node
import sys

    # BLUE = 2
    # RED = 1
    # EMPTY = 0

#Game modes:
# 1 - H vs M
# 2 - M vs H
# 3 - LM vs OM
# 4 - OM vs LM
# 5 - H vs H 



tlimit = 30
not_winner = True
humanPlayer = input("Write a color: blue or red: ")
machinePlayer = Minimax(tlimit, True)

currentMoveCoords = ()
totalPieces = 0

data_board = Board()
data_board.initPieces()

if humanPlayer == "blue":
    humanTurn = 2
    AITurn = 1
else:
    humanTurn = 1
    AITurn = 2
    root_node = Node(humanTurn, data_board, 1)
    _, best_move = machinePlayer.alphaBetaMinimax(root_node)
    data_board.changeTurn()

data_board.pp_board()

while(not_winner):
    if data_board.turn == 2:
        coords = input("Insert row and column of the tile you want to move: ")
        coords_splitted = coords.split(',')
        x_pos = int(coords_splitted[0])-1
        y_pos = int(coords_splitted[1])-1
        legal_moves = machinePlayer.generate_legal_moves(x_pos, y_pos, data_board.get_board())
        print("Recomended places to move: \n")
        data_board.pp_board(legal_moves)
        coord2move = input("Insert row and column where you want to move {} coord tile: ".format((x_pos+1, y_pos+1)))
        coord2move_splitted = coord2move.split(',')
        next_x = int(coord2move_splitted[0])-1
        next_y = int(coord2move_splitted[1])-1
        data_board.move_piece((x_pos, y_pos), (next_x, next_y))
        data_board.pp_board()

    if data_board.turn == 1:
        copy_board = Board()
        copy_board.set_board(data_board.get_board())
        root_node = Node(humanTurn, copy_board, 3)
        print("AI thinking")
        return_node, best_move = machinePlayer.alphaBetaMinimax(root_node)
        print("AI move is from {} to {}".format(best_move[0], best_move[1]))
        data_board.move_piece(best_move[0],best_move[1])
        data_board.pp_board()

    winner = data_board.detectWin()
    if winner[0] and winner[1]:
        not_winner = False
        print("Draw. End Game")
    elif winner[0]:
        not_winner = False
        print("Red wins")
    elif winner[1]:
        not_winner = False
        print("Blue wins")
    else:
        not_winner = True
    data_board.changeTurn()
        




        







 




