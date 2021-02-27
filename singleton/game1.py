# pylint: disable=too-few-public-methods
"A Game Class that uses the Leaderboard Singleton"

from leaderboard import Leaderboard
from interface_game import IGame


class Game1(IGame):
    "Game1 implements IGame"

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)
