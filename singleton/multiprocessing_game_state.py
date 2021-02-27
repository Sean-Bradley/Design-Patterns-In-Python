# pylint: disable=too-few-public-methods

"""
Singleton Use Case Example Code
"""

#import threading


class GameState():
    """The Singleton Class"""
    _instance = None

    phase = 1
    score = 100
    clock = 23
    #t = threading

    def __new__(cls):
        if cls._instance is None:
            #cls._instance = super(GameState, cls).__new__(cls)
            cls._instance = GameState
        return cls._instance

    @classmethod
    def get_status(cls):
        """An example class level method. It is static"""
        print(
            f"{id(cls._instance)} phase={cls.phase} score={cls.score} clock={cls.clock}")

        #cls.t.Timer(1.0, cls.get_status).start()

    @classmethod
    def start(cls):
        print(id(cls))