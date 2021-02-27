"A Player Object"


class Player():
    "A Player Object"

    def __init__(self, alias, balance):
        self.alias = alias
        self.balance = balance
        self.bets = []
        self.last_winnings = 0

    def place_bets(self, bets):
        "When a player places bets, its balance is deducted"
        for _ in bets:
            self.balance -= 1
        self.bets = bets

    @staticmethod
    def notify(message):
        "The player is an observer of the game"
        print(message)
