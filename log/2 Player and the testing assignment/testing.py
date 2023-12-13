import unittest
from OOP import Board, HumanPlayer, BotPlayer, Game

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = HumanPlayer("X")
        self.player2 = BotPlayer("O")

    def test_empty_board(self):
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_initialize_game_with_two_players(self):
        game = Game(self.player1, self.player2)
        self.assertEqual(game.player1.symbol, "X")
        self.assertEqual(game.player2.symbol, "O")

    def test_initialize_game_with_one_player(self):
        game = Game(self.player1, None)
        self.assertEqual(game.player1.symbol, "X")
        self.assertIsNone(game.player2)

    def test_players_take_turns(self):
        game = Game(self.player1, self.player2)
        self.assertEqual(game.current_player, self.player1)
        game.switch_player()
        self.assertEqual(game.current_player, self.player2)
        game.switch_player()
        self.assertEqual(game.current_player, self.player1)

    def test_valid_moves(self):
        self.assertTrue(self.board.is_valid_move(0, 0))
        self.assertFalse(self.board.is_valid_move(3, 0))
        self.board.make_move(0, 0, 'X')
        self.assertFalse(self.board.is_valid_move(0, 0))

    def test_check_winner(self):
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'X')
        self.board.make_move(0, 2, 'X')
        self.assertTrue(self.board.check_winner('X'))

    def test_full_board(self):
        self.board.board = [['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'X', 'O']]
        self.assertTrue(self.board.is_full())

if __name__ == '__main__':
    unittest.main()