import random
import time
import math


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
            position_value = input(
                self.letter + "\'s turn, Enter Your Move (0-8): ")
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
            position = self.minimax(game, self.letter)['position']

        return position

    def minimax(self, state, player):
        max_player = self.letter  # the players
        other_player = 'O' if player == 'X' else 'X'

        # First we want to check if the previous move is a current_winner
        # This will be our base case
        if state.current_winner == other_player:
            # we should return position and score because we need to keep track of the score

            return {'position': None,
                    'score': 1 * (state.empty_positions_num() + 1) if other_player == max_player else -1 * (state.empty_positions_num() + 1)
                    }

        elif not state.empty_position():  # no empty square
            return {'position': None,
                    'score': 0
                    }

        # main logic
        if player == max_player:
            best = {'position': None,
                    'score': -math.inf  # each score should be larger
                    }
        else:
            best = {'position': None,
                    'score': math.inf  # each score should be smaller
                    }

        for possible_move in state.available_moves():
            # step1: make a move, try that spot
            state.make_move(possible_move, player)

            # step2: recursing minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step4: update the dictionary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
