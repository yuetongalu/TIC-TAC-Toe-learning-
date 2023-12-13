#New Assignment
import random


class Board:
    """
    Represents a Tic Tac Toe board.
    Attributes:
        board (list): A list representing the 3x3 Tic Tac Toe board.
    """

    def __init__(self):
        """Initializes the board with empty spaces."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 Tic Tac Toe board

    def print_board(self):
        """Prints the current state of the board."""
        for row in self.board:
            print("|".join(row))
            print("-----")

    def make_move(self, row, col, symbol):
        """
        Attempts to place a symbol at the given position on the board.
        Args:
            row (int): The row to place the symbol (0-2).
            col (int): The column to place the symbol (0-2).
            symbol (str): The symbol to place ('X' or 'O').
        Returns:
            bool: True if the move is valid and made; False otherwise.
        >>> board = Board()
        >>> board.make_move(0, 0, 'X')
        True
        >>> board.make_move(0, 0, 'O')
        False
        """
        if self.is_valid_move(row, col):
            self.board[row][col] = symbol
            return True
        return False

    def is_valid_move(self, row, col):
        """
        Checks if the move is valid (i.e., within the board and on an empty space).
        Args:
            row (int): The row to check.
            col (int): The column to check.
        Returns:
            bool: True if the move is valid; False otherwise.
        >>> board = Board()
        >>> board.is_valid_move(0, 0)
        True
        >>> board.is_valid_move(3, 0)
        False
        """
        if 0 <= row < 3 and 0 <= col < 3:
            return self.board[row][col] == ' '
        return False

    def check_winner(self, symbol):
        """
        Checks if the given symbol has won the game.
        Args:
            symbol (str): The symbol to check ('X' or 'O').
        Returns:
            bool: True if the symbol has won; False otherwise.
        """
        # Check all winning conditions
        for i in range(3):
            # Check rows and columns
            if (
                self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol
                or self.board[0][i] == self.board[1][i] == self.board[2][i] == symbol
            ):
                return True
        # Check diagonals
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol
        ):
            return True
        return False

    def is_full(self):
        """
        Checks if the board is full (no empty spaces left).
        Returns:
            bool: True if the board is full; False otherwise.
        >>> board = Board()
        >>> board.is_full()
        False
        """
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))


class BasePlayer:
    """
    Represents a generic player in the Tic Tac Toe game.
    Attributes:
        symbol (str): The symbol assigned to the player ('X' or 'O').
    """

    def __init__(self, symbol):
        """Initializes the player with a symbol."""
        self.symbol = symbol

    def make_move(self, board):
        """
        Makes a move on the board. This method should be overridden in subclasses.
        Args:
            board (Board): The game board.
        """
        pass


class HumanPlayer(BasePlayer):

    def make_move(self, board):

        try:
            row = int(input(f"Player {self.symbol}, enter the row (0-2): "))
            col = int(input(f"Player {self.symbol}, enter the column (0-2): "))
        except ValueError:
            return False
        return board.make_move(row, col, self.symbol)


class BotPlayer(BasePlayer):


    def make_move(self, board):

        valid_moves = [(i, j) for i in range(3) for j in range(3) if board.is_valid_move(i, j)]
        print(f"Valid moves: {valid_moves}")
        row, col = random.choice(valid_moves)
        print(f"BotPlayer {self.symbol} chooses position ({row}, {col})")
        return board.make_move(row, col, self.symbol)


class Game:

    def __init__(self, player1, player2):
        """Initializes the game with two players."""
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def switch_player(self):
        """Switches the turn to the other player."""
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play(self):
        """
        Starts and manages the Tic Tac Toe game play.
        """
        while True:
            self.board.print_board()
            if not self.current_player.make_move(self.board):
                print("Invalid move, try again.")
                continue

            if self.board.check_winner(self.current_player.symbol):
                self.board.print_board()
                print(f"Player {self.current_player.symbol} wins!")
                break

            if self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break

            self.switch_player()


if __name__ == "__main__":
    # To play the game
    num_human_players = input("How many human players? (1/2): ")
    player1 = HumanPlayer("X")
    player2 = None

    if num_human_players == "1":
        player2 = BotPlayer("O")
    elif num_human_players == "2":
        player2 = HumanPlayer("O")
    else:
        print("Invalid input. Please enter 1 or 2 for the number of human players.")
        exit(1)

    game = Game(player1, player2)
    game.play()