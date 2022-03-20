import random
import time


class Player():
    def __init__(self, letter):
        # letter can be x or o
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        position = random.choice(game.available_moves())
        time.sleep(2)
        return position


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False

        while not valid_square:
            position_value = input(self.letter + "\'s turn, Enter Your Move (0-8): ")
            try:
                position = int(position_value)
                if position not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print(" Invalid input, Try Again!")

        return position


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            position = random.choice(game.available_moves())
        else:
            # smart computer uses minimax algorithm to calculate
            # the next best position based on the current state of the game
            position = self.minimax(game, self.letter)

        return position

    def minimax(self, state, letter):
        pass
