import unittest
import game


class TestGame(unittest.TestCase):
    def test_can_create_board(self):
        board = game.Board()

    def test_board_can_tell_snake_pos(self):
        board = game.Board()

        board.snakes = {51: game.Snake(23)
                , 24: game.Snake(7)}

        self.assertTrue(board.has_snake(51))
        self.assertFalse(board.has_snake(4))

    def test_board_can_tell_ladder_pos(self):
        board = game.Board()

        board.ladders = {3: 5, 6: 7}

        self.assertTrue(board.has_ladder(3))
        self.assertFalse(board.has_ladder(4))

    def test_board_can_tell_ladder_end(self):
        board = game.Board()

        board.ladders = {3: 5, 6: 7}

        self.assertEqual(board.get_ladder_end(3), 5)

    def test_board_can_tell_snake_tail(self):
        board = game.Board()
        board.snakes = {
            5: game.Snake(3),
            7: game.Snake(4),
        }

        self.assertEqual(board.get_snake_tail(5), 3)

    def test_board_raises_error_for_wrong_ladder_pos(self):
        board = game.Board()

        board.ladders = {3: 5, 6: 7}

        with self.assertRaises(game.LadderNotFoundError):
            board.get_ladder_end(23)

    def test_board_raises_error_for_wrong_snake_pos(self):
        board = game.Board()
        board.snakes = {
            5: game.Snake(3),
            7: game.Snake(4),
        }

        with self.assertRaises(game.SnakeNotFoundError):
            board.get_snake_tail(15)

    def test_dice_fair(self):

        dice = game.Dice()
        self.assertIn(dice.throw(), [1, 2, 3, 4, 5, 6])

    def test_dice_crooked(self):
        dice = game.Dice(is_crooked=True)
        self.assertIn(dice.throw(), [2, 4, 6])

    def test_green_snake(self):
        board = game.Board()
        snake = game.GreenSnake(7)
        board.snakes = {
                    17: snake,
                }

        self.assertTrue(board.has_snake(17))
        self.assertEqual(7, board.get_snake_tail(17))

        self.assertFalse(snake.is_alive())
        self.assertFalse(board.has_snake(17))
