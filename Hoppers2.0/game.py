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

if humanPlayer == "green":
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
        coords = input("Inserte row and column of the tile you want to move: ")
        coords_splitted = coords.split(',')
        legal_moves = machinePlayer.generate_legal_moves(int(coords_splitted[0])-1, int(coords_splitted[1])-1, data_board.get_board())
        print("Places to move: \n")
        data_board.pp_board(legal_moves)



        




        







 




