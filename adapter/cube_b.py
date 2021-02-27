# pylint: disable=too-few-public-methods
"A Class of Cube from Company B"
import time
from interface_cube_b import ICubeB


class CubeB(ICubeB):
    "A hypothetical Cube tool from company B"
    # a static variable indicating the last time a cube was manufactured
    last_time = int(time.time())

    def create(self, top_left_front, bottom_right_back):
        now = int(time.time())
        if now > int(CubeB.last_time + 2):
            CubeB.last_time = now
            return True
        return False  # busy
