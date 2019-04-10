"""The Command Design Pattern in Python
The command pattern is a behavioural design pattern, in which an abstraction
exists between an object that invokes a command, and the object that performs it.

This is part 2 of the Command Design Pattern tutorial,
where I create a slider, instead of the switch from part 1.
The slider also accepts a variable percentage, rather than an ON/OFF
The history also records the variable settingg
And I also add UNDO/REDO to the Invoker so that you can go backawards and forwards through time

"""

from abc import ABCMeta, abstractstaticmethod
import time


class ICommand(metaclass=ABCMeta):
    """The command interface, which all commands will implement"""

    @abstractstaticmethod
    def execute():
        """The required execute method which all command obejcts will use"""


class Slider:
    """The Invoker Class"""

    def __init__(self):
        self._commands = {}
        self._history = [(0.0, "OFF", ())]
        self._history_position = 0

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name, *args):
        if command_name in self._commands.keys():
            self._history_position += 1
            self._commands[command_name].execute(args)
            if len(self._history) == self._history_position:
                self._history.append((time.time(), command_name, args))
            else:
                self._history = self._history[:self._history_position+1]
                self._history[self._history_position] = {
                    time.time(): [command_name, args]
                }
        else:
            print(f"Command [{command_name}] not recognised")

    def undo(self):
        if self._history_position > 0:
            self._history_position -= 1
            self._commands[
                self._history[self._history_position][1]
            ].execute(self._history[self._history_position][2])
        else:
            print("nothing to undo")

    def redo(self):
        if self._history_position + 1 < len(self._history):
            self._history_position += 1
            self._commands[
                self._history[self._history_position][1]
            ].execute(self._history[self._history_position][2])
        else:
            print("nothing to REDO")


class Heater:
    """The Reciever"""

    def set_to_max(self):
        print("Heater is ON and set to MAX (100%)")

    def set_to_percent(self, *args):
        print(f"Heater is ON and set to {args[0][0]}%")

    def turn_off(self):
        print("Heater is OFF")


class SliderMaxCommand(ICommand):
    """A Command object, which implements the ICommand interface"""

    def __init__(self, heater):
        self._heater = heater

    def execute(self, *args):
        self._heater.set_to_max()


class SliderPercentCommand(ICommand):
    """A Command object, which implements the ICommand interface"""

    def __init__(self, heater):
        self._heater = heater

    def execute(self, *args):
        self._heater.set_to_percent(args[0])


class SliderOffCommand(ICommand):
    """A Command object, which implements the ICommand interface"""

    def __init__(self, heater):
        self._heater = heater

    def execute(self, *args):
        self._heater.turn_off()


if __name__ == "__main__":
    # The Client is the main python app

    # The HEATER is the Reciever
    HEATER = Heater()

    # Create Commands
    SLIDER_MAX = SliderMaxCommand(HEATER)
    SLIDER_PERCENT = SliderPercentCommand(HEATER)
    SLIDER_OFF = SliderOffCommand(HEATER)

    # Register the commands with the invoker (Switch)
    SLIDER = Slider()
    SLIDER.register("MAX", SLIDER_MAX)
    SLIDER.register("PERCENT", SLIDER_PERCENT)
    SLIDER.register("OFF", SLIDER_OFF)

    # Execute the commands that are registered on the Invoker
    SLIDER.execute("PERCENT", 10)
    SLIDER.execute("PERCENT", 20)
    SLIDER.execute("PERCENT", 30)
    SLIDER.execute("PERCENT", 40)
    SLIDER.execute("PERCENT", 50)
    SLIDER.undo()
    SLIDER.undo()
    SLIDER.undo()
    SLIDER.redo()
    SLIDER.undo()
    SLIDER.undo()
    SLIDER.execute("PERCENT", 90)
    SLIDER.execute("MAX")
    SLIDER.execute("OFF")
    SLIDER.undo()
    SLIDER.redo()

    # For fun, we can see the history
    print(SLIDER.history)
