"A Leaderboard Singleton Class"


class Leaderboard():
    "The Leaderboard as a Singleton"
    _instance = None
    _table = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = Leaderboard
        return cls._instance

    @classmethod
    def print(cls):
        "A class level method"
        print("-----------Leaderboard-----------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        print()

    @classmethod
    def add_winner(cls, position, name):
        "A class level method"
        cls._table[position] = name
