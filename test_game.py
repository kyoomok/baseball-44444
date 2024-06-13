from unittest import TestCase
from game import Game


class TestGame(TestCase):
    def test_game(self):
        game = Game()
        self.assertEqual(1,1)
