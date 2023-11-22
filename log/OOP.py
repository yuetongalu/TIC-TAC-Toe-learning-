import random

class TicTacToe:
    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def player_move(self):
        while True:
            row = int(input(f"Player {self.current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {self.current_player}, enter the column (0, 1, or 2): "))

            if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")

    def bot_move(self):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if self.board[row][col] == ' ':
                return row, col

    def make_move(self, row, col):
        self.board[row][col] = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:
            if self.current_player == 'X':
                row, col = self.player_move()
            else:
                print("Bot is making a move...")
                row, col = self.bot_move()

            self.make_move(row, col)
            self.print_board()

            if self.check_winner(self.current_player):
                print(f"Player {self.current_player} wins!")
                break

            if self.is_board_full():
                print("It's a tie!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()