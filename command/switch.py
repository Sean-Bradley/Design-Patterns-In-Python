"""
The Switch (Invoker) Class.
You can flick the switch and it then invokes a registered command
"""
from datetime import datetime
import time


class Switch:
    "The Invoker Class."

    def __init__(self):
        self._commands = {}
        self._history = []

    def show_history(self):
        "Print the history of each time a command was invoked"
        for row in self._history:
            print(
                f"{datetime.fromtimestamp(row[0]).strftime('%H:%M:%S')}"
                f" : {row[1]}"
            )

    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(), command_name))
        else:
            print(f"Command [{command_name}] not recognised")

    def replay_last(self, number_of_commands):
        "Replay the last N commands"
        commands = self._history[-number_of_commands:]
        for command in commands:
            self._commands[command[1]].execute()
            #or if you want to record these replays in history
            #self.execute(command[1])
