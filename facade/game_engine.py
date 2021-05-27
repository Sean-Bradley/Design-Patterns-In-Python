"The Game Engine"
import time
from decimal import Decimal
from wallets import Wallets
from reports import Reports


class GameEngine():
    "The Game Engine"
    _instance = None
    _start_time: int = 0
    _clock: int = 0
    _entries: list[tuple[str, Decimal]] = []  # Python 3.9
    # _entries = []  # Python 3.8 or earlier
    _game_open = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = GameEngine
            cls._start_time = int(time.time())
            cls._clock = 60
        return cls._instance

    @classmethod
    def get_game_state(cls) -> dict:
        "Get a snapshot of the current game state"
        now = int(time.time())
        time_remaining = cls._start_time - now + cls._clock
        if time_remaining < 0:
            time_remaining = 0
            cls._game_open = False
        return {
            "clock": time_remaining,
            "game_open": cls._game_open,
            "entries": cls._entries
        }

    @classmethod
    def submit_entry(cls, user_id: str, entry: Decimal) -> bool:
        "Submit a new entry for the user in this game"
        now = int(time.time())
        time_remaining = cls._start_time - now + cls._clock
        if time_remaining > 0:
            if Wallets.get_balance(user_id) > Decimal('1'):
                if Wallets.adjust_balance(user_id, Decimal('-1')):
                    cls._entries.append((user_id, entry))
                    Reports.log_event(
                        f"New entry `{entry}` submitted by `{user_id}`")
                    return True
                Reports.log_event(
                    f"Problem adjusting balance for `{user_id}`")
                return False
            Reports.log_event(f"User Balance for `{user_id}` to low")
            return False
        Reports.log_event("Game Closed")
        return False
