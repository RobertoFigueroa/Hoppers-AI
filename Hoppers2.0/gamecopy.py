from types import coroutine
from board import Board
from dummyminmax import Minimax
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
m_vs_m = int(input("Do you want machine vs machine offline inserte 1: "))
humanPlayer = int(input("Write 1 or 2 to play in that order: "))
corner = int(input("Write zero to start in up corner or any other key for start down corner: "))
machinePlayer = Minimax(tlimit, True)
data_board = Board()
data_board.initPieces()
AI_root = 1

if m_vs_m == 1:
    while not_winner:
        copy_board = Board()
        copy_board.set_board(data_board.get_board())
        root_node = Node(data_board.turn, copy_board, 3)
        print("AI thinking")
        return_node, best_move = machinePlayer.alphaBetaMinimax(root_node)
        print("AI move  from {} to {}".format(best_move[0], best_move[1]))
        data_board.move_piece(best_move[0],best_move[1])
        data_board.pp_board()

        winner = data_board.detectWin()
        if winner[0] and winner[1]:
            not_winner = False
            print("Draw. End Game")
        elif winner[0]:
            not_winner = False
            print("Up corner wins")
        elif winner[1]:
            not_winner = False
            print("Down corner wins")
        else:
            not_winner = True
        data_board.changeTurn()
        machinePlayer.prevSpots = []

print("Game over")
sys.exit()


if corner == 0 and humanPlayer == 1:
    data_board.setTurn(1)
    AI_root = 2
elif corner == 0 and humanPlayer == 2:
    data_board.setTurn(2)
    AI_root = 2
elif corner != 0 and humanPlayer == 1:
    data_board.setTurn(1)
    AI_root = 1
else:
    data_board.setTurn(2)
    AI_root = 1


data_board.pp_board()


while(not_winner):
    if data_board.turn == 1:
        coords = input("Insert row and column of the tile you want to move: ")
        coords_splitted = coords.split(',')
        x_pos = int(coords_splitted[0])-1
        y_pos = int(coords_splitted[1])-1
        legal_moves = machinePlayer.generate_legal_moves(x_pos, y_pos, data_board.get_board())
        print("Legal moves", legal_moves)
        print("Recomended places to move: \n")
        data_board.pp_board(legal_moves)
        coord2move = input("Insert row and column where you want to move {} coord tile: ".format((x_pos+1, y_pos+1)))
        coord2move_splitted = coord2move.split(',')
        next_x = int(coord2move_splitted[0])-1
        next_y = int(coord2move_splitted[1])-1
        data_board.move_piece((x_pos, y_pos), (next_x, next_y))
        #data_board.pp_board()

    if data_board.turn == 2:
        copy_board = Board()
        copy_board.set_board(data_board.get_board())
        root_node = Node(AI_root, copy_board, 3)
        print("AI thinking")
        return_node, best_move = machinePlayer.alphaBetaMinimax(root_node)
        print("AI move  from {} to {}".format(best_move[0], best_move[1]))
        data_board.move_piece(best_move[0],best_move[1])
        data_board.pp_board()
        machinePlayer.prevSpots = []


    winner = data_board.detectWin()
    if winner[0] and winner[1]:
        not_winner = False
        print("Draw. End Game")
    elif winner[0]:
        not_winner = False
        print("Up corner wins")
    elif winner[1]:
        not_winner = False
        print("Down corner wins")
    else:
        not_winner = True
    data_board.changeTurn()
    machinePlayer.prevSpots = []
    





        







 




