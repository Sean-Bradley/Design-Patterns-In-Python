"The Facade Example Use Case"
import time
from decimal import Decimal
from game_api import GameAPI

USER = {"user_name": "sean"}
USER_ID = GameAPI.register_user(USER)

time.sleep(1)

GameAPI.submit_entry(USER_ID, Decimal('5'))

time.sleep(1)

print()
print("---- Gamestate Snapshot ----")
print(GameAPI.game_state())

time.sleep(1)

HISTORY = GameAPI.get_history()

print()
print("---- Reports History ----")
for row in HISTORY:
    print(f"{row} : {HISTORY[row][0]} : {HISTORY[row][1]}")

print()
print("---- Gamestate Snapshot ----")
print(GameAPI.game_state())
