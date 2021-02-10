from hoppers import Hoppers
from minimax import findPath, bestScore
#setting up the game
print("Welcome to hoppers game!")
game = Hoppers(10, 10)
play_mode = int(input("Choose a number: \n1.Human vs AI\n2.AI vs AI:  "))
game.print_board()
canPlay = True
player_turn = 0
if play_mode == 1:
    while canPlay:
        print("Turn: Player 1 (Human)")
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
        if game.check_for_winner() == 1:
            print("Player 1 won")
            canPlay = False
            break
        game.print_board()
        print("Turn: Player 2 (AI)")
        print("game status:", game.check_for_winner())
        ai_place2move = bestScore(game,1)
        if ai_place2move != None:
            game.move(ai_place2move[0],ai_place2move[1],ai_place2move[2],ai_place2move[3],'O')
        if game.check_for_winner() == -1:
            print("Player 2 won")
            canPlay = False
            break
        game.print_board()
        print(ai_place2move)
else:
    while canPlay:
        player_turn = (player_turn+1) % 2
        print("Turn: AI 1")
        ai1_place2move = bestScore(game, player_turn)
        if ai1_place2move != None:
            game.move(ai1_place2move[0], ai1_place2move[1], ai1_place2move[2], ai1_place2move[3], 'O')
        game.print_board()
        if game.check_for_winner() == -1:
            print("AI 1 won")
            canPlay = False
            break
        print("turno -->", player_turn)
        print("Turn AI 2")
        player_turn = (player_turn+1) % 2
        ai2_place2move = bestScore(game,player_turn)
        if ai2_place2move != None:
            game.move(ai2_place2move[0], ai2_place2move[1], ai2_place2move[2], ai2_place2move[3], 'X')
        game.print_board()
        print("turno -->", player_turn)
        if game.check_for_winner() == 1:
            print("AI 2 won")
            canPlay = False
            break

        