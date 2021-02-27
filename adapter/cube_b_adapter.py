# pylint: disable=too-few-public-methods
"An adapter for CubeB so that it can be used like Cube A"
from interface_cube_a import ICubeA
from cube_b import CubeB


class CubeBAdapter(ICubeA):
    "Adapter for CubeB that implements ICubeA"

    def __init__(self):
        self.cube = CubeB()
        self.width = self.height = self.depth = 0

    def manufacture(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

        success = self.cube.create(
            [0-width/2, 0-height/2, 0-depth/2],
            [0+width/2, 0+height/2, 0+depth/2]
        )
        return success
