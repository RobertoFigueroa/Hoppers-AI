from types import coroutine
from board import Board
from minimax import Minimax
from node import Node
import sys


d_board = Board()

d_board.initPieces()

d_board.board[0][0] = 2
d_board.board[9][9] = 1

d_board.print_board()
w = d_board.detectWin()

print(w) #expected (True, True)


# m = Minimax(30, True)

# lm = m.generate_legal_moves(1, 1, d_board.get_board())
# d_board.move_piece((1,1), (3,3))
# lm = m.generate_legal_moves(2, 2, d_board.get_board())

# d_board.move_piece((2,2), (4,4))

# d_board.pp_board()


# lm = m.generate_legal_moves(3, 3, d_board.get_board())


# print(lm)