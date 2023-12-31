import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o. (ie playe x and o)
        self.letter = letter

        #we want all players to get their next move given a game
        def get_move(self, game):
            pass

class RandomComputerPlayer(Player):
    def __init(self, letter):
        #super method to allow child function inherits all the functionality of the parenet function
        super().__init(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HuamnPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #we are gonna to check that this is a correct value by trying to cast
            #it to an integer, and if it's not, then we say its invalid
            #if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #If these are successful, then yay!
            except ValueError:
                print('Invalid sqaure. Try again.')

        return val
