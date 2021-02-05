from hoppers import Hoppers
from minimax import findPath, bestScore
#setting up the game
print("Welcome to hoppers game!")
game = Hoppers(10, 10)
game.print_board()

playerTurn = 1
while True:
    print("Turn: Player 1")
    coin2move = input("Type wich coin you want to move separated by commas: ")
    coin_coords = coin2move.split(',')
    options = findPath(game.board, 10, int(coin_coords[0])-1, int(coin_coords[1])-1,'X', False)
    print("options: ", options)
    place2move = input("Type where you want to move separated by comma: ")
    next_coords = place2move.split(',')
    #imagine that player is intelligent and no need for checking the value
    game.move(
        int(coin_coords[0]),
        int(coin_coords[1]),
        int(next_coords[0]),
        int(next_coords[1]), 
        'X')
    game.print_board()
    print("Turn: Player 2 (Soon AI)")
    print("game status:", game.check_for_winner())
    ai_place2move = bestScore(game)
    if ai_place2move != None:
       game.move(ai_place2move[0],ai_place2move[1],ai_place2move[2],ai_place2move[3],'O')
    game.print_board()
    print(ai_place2move)
    