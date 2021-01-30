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

    def move(self, x, y, symbol):
        x = x-1
        y = y-1
        if self.board[x][y] == '_':
            self.board[x][y] = symbol
            return True
        else:
            return False

h = Hoppers(10, 10)
h.move(1,1,'X')
h.move(1,1,'X')
h.move(1,4,'O')

h.print_board()
