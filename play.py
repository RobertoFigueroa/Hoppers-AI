from hoppers import Hoppers

#setting up the game
print("Welcome to hoppers game!")
game = Hoppers(10, 10)
game.print_board()

playerTurn = 1
while True:
    print("Turn: Player 1")
    coin2move = input("Type wich coin you want to move separated by commas: ")
    coin_coords = coin2move.split(',')
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
