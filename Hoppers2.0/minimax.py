from node import Node
from board import Board
import numpy as np
import time
import math

class Minimax:

    def __init__(self, timeLimit, alphaBeta):
        self.move_list = []
        self.piece_selected = 0
        self.selected_coords = ()
        self.prevSpots = []
        self.timeLimit = timeLimit
        self.start = 0
        self.end = 0
        self.prunes = 0
        self.boards = 0
        self.alphaBeta = alphaBeta

    def hop_search(self, row, col, board):
        row_offsets = [-1, 0, 1]
        col_offsets = [-1, 0, 1]
        jumps = []

        gameboard = Board()

        for row_offset in row_offsets:
            for col_offset in col_offsets:
                if (row + row_offset) >= len(board) or (col + col_offset) >= len(board):
                    continue
                if (row + row_offset) < 0 or (col + col_offset) < 0:
                    continue

                if (row + row_offset) == row and (col + col_offset) == col:
                    continue
                
                if ( board[row + row_offset][col + col_offset] != 0):
                    row_jump_offset = row + 2*row_offset
                    col_jump_offset = col + 2*col_offset

                    if (row_jump_offset) >= len(board) or (col_jump_offset) >= len(board):
                        continue
                    if (row_jump_offset) < 0 or (col_jump_offset) < 0:
                        continue
                
                    if(board[row + 2*row_offset][col+2*col_offset] == 0 and (row + 2*row_offset, col+2*col_offset) not in self.prevSpots):
                    
                        if(board[row][col] == 1 and (row,col) not in gameboard.redCorner):
                            if((row_jump_offset, col_jump_offset) in gameboard.redCorner):
                                continue
                    
                        if(board[row][col] == 2 and (row, col) not in gameboard.blueCorner):
                            if((row_jump_offset, col_jump_offset) in gameboard.blueCorner):
                                continue
                    
                        self.prevSpots.append((row, col))
                        jumps.append((row + 2*row_offset, col + 2*col_offset))

                        future_hops = self.hop_search(row_jump_offset, col_jump_offset, board)

                        jumps.extend(future_hops)

                        self.move_list.extend(future_hops)

        return jumps

    def generate_legal_moves(self, row, col, board):
        gameboard = Board()

        if row >= len(board) or col >= len(board):
            print("That position is out of bounds")
            return

        if row < 0 or col < 0:
            print("That position is out of bounds")
            return
        
        if board[row][col] == 0:
            print("There isn't a piece there to move.")
            return
        
        row_offsets = [-1, 0, 1]
        col_offsets = [-1, 0, 1]

        legal_moves = []
        blocked_spaces = []

        for row_offset in row_offsets:
            for col_offset in col_offsets:

                if (row + row_offset) >= len(board) or (col + col_offset) >= len(board[0]):
                    continue
                
                if (row + row_offset) == row and (col + col_offset) == col:
                    continue
                
                if (row + row_offset) < 0 or (col + col_offset) < 0:
                    continue
                
                if (board[row + row_offset][col + col_offset] == 0):
                    if (board[row][col] == 1 and (row, col) not in gameboard.redCorner):
                        if ((row + row_offset, col + col_offset) in gameboard.redCorner):
                            continue
                
                    if (board[row][col] == 2 and (row, col) not in gameboard.blueCorner):
                        if ((row + row_offset, col + col_offset) in gameboard.blueCorner):
                            continue

                    legal_moves.append((row + row_offset, col + col_offset))
                else:
                    blocked_spaces.append((row + row_offset, col + col_offset))
        
        legal_moves.extend(self.hop_search(row, col, board))

        self.move_list.extend(legal_moves)

        return legal_moves


    def clear_move_list(self):
        self.move_list = []

    def distance(self, p1, p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    
    def utility(self, node):
        board = node.board
        winCheck = board.detectWin()
        data_board = board.get_board()
        value = 0
        red = 0
        blue = 0

        for col in range(board.get_width()):
            for row in range(board.get_width()):
                tile =  data_board[row][col]

                #blue piece
                if tile == 2:
                    distanceList = [self.distance((row, col), goals) for goals in board.redCorner if data_board[goals[0]][goals[1]] != 2]
                    blue += max(distanceList) if len(distanceList) else -100

                elif tile == 1:
                   distanceList = [self.distance((row, col), goals) for goals in board.blueCorner if data_board[goals[0]][goals[1]] != 1]
                   red += max(distanceList) if len(distanceList) else - 100
        if node.player == 1:
            value = red/blue
        else:
            value = blue/red

        if winCheck[0]:
            value = float("inf")
        elif winCheck[1]:
            value = float("inf")
        
        return value

    def alphaBetaMinimax(self, node):
        self.start = time.time()
        max_node, best_move = self.maxValue(node, float("-inf"), float("inf"))
        data_board = node.get_board()
        data_board.move_piece(best_move[0], best_move[1])
        print("Took", self.end - self.start, "seconds to choose a move")
        print("Pruned", self.prunes, " branches")
        print("Generated", self.boards, " boards")
        self.prunes = 0
        self.boards = 0
        data_board.chosenMove = best_move
        data_board.changeTurn()
        return max_node, best_move

    def maxValue(self, node, alpha, beta):
        self.end =  time.time()

        board = node.get_board()
        win_detect = board.detectWin()
        best_move = None
        if(win_detect[0] == True or win_detect[1] == True or node.get_depth() <= 0 or self.end - self.start > self.timeLimit):
            evaluation = self.utility(node)
            node.set_value(evaluation)
            return node, best_move

        player = node.get_player()
        next_player = player

        if player == 1:
            player_positions = board.get_blue_positions()
        elif player == 2:
            player_positions = board.get_red_positions()
        
        value = float("-inf")
        data_board = board.get_board()

        for move in player_positions:
            legal_moves = self.generate_legal_moves(move[0], move[1], data_board)
            if len(legal_moves) == 0:
                continue
            
            for legal_move in legal_moves:
                self.end = time.time()
                if(self.end -self.start > self.timeLimit):
                    return node, best_move
                self.boards += 1
                board_copy = Board()
                board_copy.set_board(data_board)

                board_copy.move_piece(move, legal_move)

                next_node = Node(player, board_copy, node.get_depth() -1)

                next_node.move = (move, legal_move)

                child_node, _ = self.minValue(next_node, alpha, beta)

                board_copy.move_piece(legal_move, move)

                if(value < child_node.get_value()):
                    moveFrom = move
                    moveTo = legal_move
                    best_move = (moveFrom, moveTo)
                value = max(value, child_node.get_value())

                return_node = next_node 

                if value > beta and self.alphaBeta:
                    self.prunes += 1
                    return_node.set_value(beta)
                    return return_node, None

                alpha = max(alpha, value)

        return_node.set_value(value)
        return return_node, best_move


    def minValue(self, node, alpha, beta):
        self.end =  time.time()

        board = node.get_board()
        win_detect = board.detectWin()
        best_move = None
        if(win_detect[0] == True or win_detect[1] == True or node.get_depth() <= 0 or self.end - self.start > self.timeLimit):
            evaluation = self.utility(node)
            node.set_value(evaluation)
            return node, best_move

        player = node.get_player()
        next_player = player

        if player == 1:
            player_positions = board.get_blue_positions()
        elif player == 2:
            player_positions = board.get_red_positions()
        
        value = float("inf")
        data_board = board.get_board()

        for move in player_positions:
            legal_moves = self.generate_legal_moves(move[0], move[1], data_board)
            if len(legal_moves) == 0:
                continue
            
            for legal_move in legal_moves:
                self.end = time.time()
                if(self.end -self.start > self.timeLimit):
                    return node, best_move
                self.boards += 1
                board_copy = Board()
                board_copy.set_board(data_board)

                board_copy.move_piece(move, legal_move)

                next_node = Node(player, board_copy, node.get_depth() -1)

                next_node.move = (move, legal_move)

                child_node, _ = self.maxValue(next_node, alpha, beta)

                board_copy.move_piece(legal_move, move)

                if(value > child_node.get_value()):
                    moveFrom = move
                    moveTo = legal_move
                    best_move = (moveFrom, moveTo)
                value = min(value, child_node.get_value())

                return_node = next_node 

                if value < alpha and self.alphaBeta:
                    self.prunes += 1
                    return_node.set_value(value)
                    return return_node, None

                beta = min(beta, value)

        return_node.set_value(value)
        return return_node, best_move




                

