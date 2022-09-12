from player import HumanPlayer, ComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        # simple board or 3x3
        self.board = [' ' for _ in range(0, 9)]
        self.current_winner = None  # keeping track who wins

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_position(self):
        return ' ' in self.board

    def empty_positions_num(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # player wins when any 3 sides have the same letter
        # checking rows
        rows_index = square // 3
        row = self.board[rows_index*3: (rows_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # checking columns
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # checking diagonally
        # diagonals contains position of even number
        # 0, 2, 4, 6, 8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right diagonal

            if all([spot == letter for spot in diagonal1]):
                return True

            if all([spot == letter for spot in diagonal2]):
                return True

        # if all check fail then return False
        return False


def play(game, player_x, player_o, print_game=True):
    # returns winner of the game or none or tie
    if print_game:
        game.print_board_nums()

    letter = 'X'

    # iterate till a player wins or no empty positions remaining
    while game.empty_position():
        if letter == 'X':
            square = player_x.get_move(game)
        else:
            square = player_o.get_move(game)

        # let's make a moves
        if game.make_move(square, letter):
            if print_game:
                print(letter + " makes moves on position " + str(square))
                game.print_board()
                print()  # just a new line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

        # to switch players..
        letter = 'O' if letter == 'X' else 'X'

    # when a games Tied
    print("It's a tie!")


if __name__ == "__main__":

    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    o_smart_player = SmartComputerPlayer('O')

    game = TicTacToe()
    play(game, x_player, o_smart_player, print_game=True)
