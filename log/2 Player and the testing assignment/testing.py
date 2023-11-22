import unittest
from OOP import Board, HumanPlayer, BotPlayer, Game

class TestTicTacToe(unittest.TestCase):
    def test_game_init_with_empty_board(self):
        game = Game(HumanPlayer("X"), BotPlayer("O"))
        self.assertTrue(all(board == [' '] * 9 for board in game.board.board))

    def test_game_init_with_players(self):
        player1 = HumanPlayer("X")
        player2 = BotPlayer("O")
        game = Game(player1, player2)
        self.assertEqual(game.player1, player1)
        self.assertEqual(game.player2, player2)

    def test_players_assigned_unique_pieces(self):
        player1 = HumanPlayer("X")
        player2 = BotPlayer("O")
        self.assertNotEqual(player1.symbol, player2.symbol)

    def test_alternate_turns(self):
        game = Game(HumanPlayer("X"), BotPlayer("O"))
        game.play()
        self.assertEqual(game.current_player, game.player2)

    def test_winning_end_of_game_detected(self):
        # Create a winning scenario
        game = Game(HumanPlayer("X"), HumanPlayer("O"))
        game.board.make_move(0, 0, "X")
        game.board.make_move(0, 1, "O")
        game.board.make_move(1, 1, "X")
        game.board.make_move(1, 0, "O")
        game.board.make_move(2, 2, "X")
        self.assertTrue(game.board.check_winner("X"))

    def test_draw_game_identified(self):
        # Create a draw scenario
        game = Game(HumanPlayer("X"), HumanPlayer("O"))
        game.board.make_move(0, 0, "X")
        game.board.make_move(0, 1, "O")
        game.board.make_move(0, 2, "X")
        game.board.make_move(1, 0, "O")
        game.board.make_move(1, 1, "X")
        game.board.make_move(1, 2, "O")
        game.board.make_move(2, 0, "O")
        game.board.make_move(2, 1, "X")
        game.board.make_move(2, 2, "O")
        self.assertTrue(game.board.is_full())
        self.assertFalse(game.board.check_winner("X"))
        self.assertFalse(game.board.check_winner("O"))

    def test_players_can_play_only_in_viable_spots(self):
        game = Game(HumanPlayer("X"), HumanPlayer("O"))
        game.board.make_move(0, 0, "X")
        self.assertFalse(game.board.make_move(0, 0, "O"))

    def test_correct_game_winner_detected(self):
        # Create a winning scenario
        game = Game(HumanPlayer("X"), HumanPlayer("O"))
        game.board.make_move(0, 0, "X")
        game.board.make_move(0, 1, "O")
        game.board.make_move(1, 1, "X")
        game.board.make_move(1, 0, "O")
        game.board.make_move(2, 2, "X")
        self.assertEqual(game.current_player.symbol, "X")
        self.assertTrue(game.board.check_winner("X"))

if __name__ == "__main__":
    unittest.main()
