import numpy as np

class Board:

    BLUE = 2
    RED = 1
    EMPTY = 0

    def __init__(self, size=10):
        self.size = size
        self.turn = 2
        self.board = np.full((self.size,self.size), self.EMPTY)
        self.blueCorner = []
        self.redCorner = []
        
        #self.initPieces()
        self.getRedCorner()
        self.getBlueCorner()
        self.chosenMove = 0

    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


    def detectWin(self):
        blueWins = False
        redWins = False

        #check if all the tiles in blue corner are filled with red
        for coord in self.blueCorner:
            if self.get_piece_at(coord[0], coord[1]) == False or self.get_piece_at(coord[0],coord[1]) == 2:
                redWins = False
                break
            elif self.get_piece_at(coord[0], coord[1]) == 1:
                redWins = True
        for coord in self.redCorner:
            if self.get_piece_at(coord[0], coord[1]) == False or self.get_piece_at(coord[0], coord[1]) == 1:
                blueWins = False
                break
            elif self.get_piece_at(coord[0], coord[1]) == 2:
                blueWins = True

        return (redWins, blueWins)
    
    def get_piece_at(self, row, col):
        return self.board[row][col]


    def get_board(self):
        return self.board

    def initPieces(self):
        for i in range(5):
            self.board[i,:5-i] = self.RED
        for j in range(5,10):
            self.board[j,(5+9-j):10] = self.BLUE

    def getRedCorner(self):
        points = np.where(self.board == self.RED)
        for i in zip(points[0],points[1]):
            self.redCorner.append(i)
    
    def getBlueCorner(self):
        points = np.where(self.board == self.BLUE)
        for i in zip(points[0], points[1]):
            self.blueCorner.append(i)

    def get_height(self):
        return self.size
    
    def get_width(self):
        return self.size
    
    def move_piece(self, start_pos, end_pos):
        player = self.remove_piece_at(start_pos[0], start_pos[1])
        self.place_piece(player, end_pos[0], end_pos[1])
    
    def remove_piece_at(self, row, col):
        player = self.board[row][col]
        self.board[row][col] = self.EMPTY
        return player

    def place_piece(self, player, row, col):
        self.board[row][col] = player

    def print_board(self):
        print(self.board)
    
    def get_red_positions(self):
        red_pos_list = []
        points = np.where(self.board == self.RED)
        for i in zip(points[0], points[1]):
            red_pos_list.append(i)
        return red_pos_list

    def get_blue_positions(self):
        blue_pos_list = []
        points = np.where(self.board == self.BLUE)
        for i in zip(points[0],points[1]):
            blue_pos_list.append(i)
        return blue_pos_list

    def set_board(self, new_board):
        self.board = np.copy(new_board)
    

    
