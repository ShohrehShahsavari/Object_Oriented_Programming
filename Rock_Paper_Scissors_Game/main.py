from classes import *

if __name__ == '__main__':
    game = Game()
    player1, player2 = game.start_game()
    
    if player1 and player2:
        player1_choice = player1.move()
        player2_choice = player2.move()
        
    
    result = game.evaluate_game(player1_choice, player2_choice)
    print (f"player1: {player1}\tplayer2: {player2}\nResult: {result}")    
     