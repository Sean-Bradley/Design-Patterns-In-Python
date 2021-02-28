"""
A Command object, that implements the ISwitch interface and runs the
command on the designated receiver
"""
from interface_switch import ISwitch


class SwitchOffCommand(ISwitch):  # pylint: disable=too-few-public-methods
    "Switch Off Command"

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()
