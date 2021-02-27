"Adapter Example Use Case"

import time
import random
from cube_a import CubeA
from cube_b_adapter import CubeBAdapter


# client
TOTALCUBES = 5
COUNTER = 0
while COUNTER < TOTALCUBES:
    # produce 5 cubes from which ever supplier can manufacture it first
    WIDTH = random.randint(1, 10)
    HEIGHT = random.randint(1, 10)
    DEPTH = random.randint(1, 10)
    CUBE = CubeA()
    SUCCESS = CUBE.manufacture(WIDTH, HEIGHT, DEPTH)
    if SUCCESS:
        print(
            f"Company A building Cube id:{id(CUBE)}, "
            f"{CUBE.width}x{CUBE.height}x{CUBE.depth}")
        COUNTER = COUNTER + 1
    else:  # try other manufacturer
        print("Company A is busy, trying company B")
        CUBE = CubeBAdapter()
        SUCCESS = CUBE.manufacture(WIDTH, HEIGHT, DEPTH)
        if SUCCESS:
            print(
                f"Company B building Cube id:{id(CUBE)}, "
                f"{CUBE.width}x{CUBE.height}x{CUBE.depth}")
            COUNTER = COUNTER + 1
        else:
            print("Company B is busy, trying company A")
    # wait some time before manufacturing a new cube
    time.sleep(1)

print(f"{TOTALCUBES} cubes have been manufactured")
