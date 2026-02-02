from abc import ABC,  abstractmethod
from random import choice

class PlayerBase(ABC):
    choices = ['r', 'p', 's']
    @abstractmethod
    def move(self):
        pass

    
class Humanplayer(PlayerBase):
    def __init__(self):
        super().__init__()
        self.current_choice = None
        
    def move(self):
        user_input = input('Enter your chice(r, p, s): ').strip()
        if user_input in self.choices:
            self.current_choice = user_input
            return user_input
        else:
            print('Invalid inputplease enter(r, p, s)')
    def __str__(self):
        return f'HumanPlayer choice: {self.current_choice}'

class Machinplayer(PlayerBase):
    def __init__(self):
        super().__init__()
        self.current_choice = None

    def move(self):
        self.current_choice = choice(self.choices)
        return self.current_choice
    
    def __str__(self):
        return f'MachinPlayer choice: {self.current_choice}'
    
class Game():
    @staticmethod
    def start_game():
        game_type = input('Enter game_type ("s" for single player "m" for multiplayer): ').strip()
        if game_type == 's':
            p1 = Humanplayer()
            p2 = Machinplayer()
        elif game_type == 'm':
            p1 = Humanplayer()
            p2 = Humanplayer()
        else:
            print('Invalid input please enter "s" or "m": ')
        return p1, p2
    
    @staticmethod
    def evaluate_game(player1, player2):
        if player1 == player2:
            return 'Equal point'
        elif player1 == 'r':
            if player2 == 'p':
                return 'player1 win'
            elif player2 == 's':
                return 'player2 win'
        
        elif player1 == 'p':
            if player2 == 'r':
                return 'player1 win'
            elif player2 == 's':
                return 'player2 win'
            
        elif player1 == 's':
            if player2 == 'r':
                return 'player2 win'
            elif player2 == 'p':
                return 'player1 win'
        else:
            return 'Invalid input'
