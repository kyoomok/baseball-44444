from unittest import TestCase
from game import Game


class TestGame(TestCase):
    def test_game(self):
        game = Game()
        self.assertEqual(1,1)

    def test_exception_when_input_is_none(self):
        game = Game()
        with self.assertRaises(TypeError):
            game.guess(None)
