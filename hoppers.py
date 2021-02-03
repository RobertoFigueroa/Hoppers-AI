class Hoppers(object):


    def __init__(self, width, height):
        self.width = width
        self.height = height #no need of this because we can assume that the board is square
        self.first_player_symbol = 'X'
        self.second_player_symbol = 'O'
        self.free_space_symbol = '_'
        self.board = []
        for i in range(self.width):
            self.board.append([])
            for j in range(self.height):
                self.board[i].append('_')
        self.fill_board()

    def fill_board(self):
        first_player_columns = 5
        for i in range(5):
            for j in range(first_player_columns):
                self.board[i][j] = self.first_player_symbol
            first_player_columns -= 1
        second_player_columns = 9
        for i in range(5,10):
            for j in range(second_player_columns,10):
                self.board[i][j] = self.second_player_symbol
            second_player_columns -= 1

    def check_for_winner(self):
        first_player_columns = 5
        first_player_coins = 0
        second_player_coins = 0
        free_space_coins = 0
        for i in range(5):
            for j in range(first_player_columns):
                if self.board[i][j] == self.first_player_symbol:
                   first_player_coins += 1
                if self.board[i][j] == self.free_space_symbol:
                    free_space_coins += 1
            first_player_columns -= 1
        
        if first_player_coins < 15 and free_space_coins == 0:
            return 1 #1 Means first player won

        free_space_coins = 0   
        second_player_columns = 9
        for i in range(5,10):
            for j in range(second_player_columns,10):
                if self.board[i][j] == self.second_player_symbol:
                    second_player_coins += 1
                if self.board[i][j] == self.free_space_symbol:
                    free_space_coins += 1
            second_player_columns -= 1

        if second_player_coins < 15 and free_space_coins == 0:
            return -1 #means second player won
        
        return 0 #no winner



    def print_board(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.board[i][j], end='  ')
            print()

    def move(self,currentX, currentY, x, y, symbol):
        if x > 0 or x <= 10 or y > 0 or y <= 10:
            x -= 1
            y -= 1
            currentX -= 1
            currentY -= 1
            if self.board[x][y] == '_':
                self.board[x][y] = symbol
                self.board[currentX][currentY] = '_'
                return True
            else:
                return False
        else:
            return False

    def coins_position(self, isAI=True): #mayb this function could be more genera 
        positions = []
        if isAI:
            second_player_columns = 9
            for i in range(self.width):
                for j in range(self.height):
                    if self.board[i][j] == self.second_player_symbol: #here, this could be more general not just for secon plaer symbol
                        positions.append((i,j))
                second_player_columns -= 1
            return positions
        else:
            first_player_columns = 5
            for i in range(5):
                for j in range(first_player_columns):
                    if self.board[i][j] == self.first_player_symbol:
                        positions.append((i,j))
                first_player_columns -= 1
            return positions



