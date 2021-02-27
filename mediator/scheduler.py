"A Scheduler"
from interface_game_engine import IGameEngine


class Scheduler(IGameEngine):
    "The scheduler implements some of the Mediator methods"

    def __init__(self, game_engine):
        self._game_engine = game_engine

    def new_game(self):
        self._game_engine.new_game()

    def add_player(self, player):
        "not implemented in the scheduler"

    def list_winners(self):
        "not implemented in the scheduler"

    def calculate_winners(self):
        self._game_engine.calculate_winners()

    def notify_winners(self):
        self._game_engine.notify_winners()

    def game_result(self):
        "not implemented in the game client"
