class Hoppers(object):


    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(self.width):
            self.board.append([])
            for j in range(self.height):
                self.board[i].append('_')
        self.fill_board()

    def fill_board(self,p1='X', p2='O'):
        first_player_columns = 5
        for i in range(5):
            for j in range(first_player_columns):
                self.board[i][j] = p1
            first_player_columns -= 1
        second_player_columns = 9
        for i in range(5,10):
            for j in range(second_player_columns,10):
                self.board[i][j] = p2
            second_player_columns -= 1

    def print_board(self):
        print
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

