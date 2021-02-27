from multiprocessing import Process
from game_state import GameState
import time

GAMESTATE = GameState()

# start 3 processes all using the GAMESTATE singleton
COUNT = 2
PROCESSES = {}
for x in range(COUNT):
    PROCESSES[x] = Process(
        target=GAMESTATE.get_status()
    )

GAMESTATE.start()

# modify the score after 3 seconds
time.sleep(3)
GAMESTATE.score = 200

