"""
Observer Design Pattern
"""

from abc import ABCMeta, abstractmethod
from enum import Enum
import time


class WeatherType(Enum):
    SUNNY = 1
    RAINY = 2
    WINDY = 3
    COLD = 4


class Weather:
    """Observable"""

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, weather_type):
        for observer in self._observers:
            observer.notify(weather_type)


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(weather_type):
        """Update all the subscribed observers"""


class BBCWeather(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, weather_type):
        print(f"{__class__} : {repr(weather_type)}")


class ABCWeather(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, weather_type):
        print(f"{__class__} : {repr(weather_type)}")


class NBCWeather(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, weather_type):
        print(f"{__class__} : {repr(weather_type)}")


if __name__ == "__main__":

    WEATHERSERVICE = Weather()

    BBCWEATHER = BBCWeather(WEATHERSERVICE)
    ABCWEATHER = ABCWeather(WEATHERSERVICE)
    NBCWEATHER = NBCWeather(WEATHERSERVICE)

    WEATHERSERVICE.notify(WeatherType.RAINY)
    WEATHERSERVICE.unsubscribe(BBCWEATHER)
    time.sleep(2)
    WEATHERSERVICE.notify(WeatherType.SUNNY)
    WEATHERSERVICE.unsubscribe(NBCWEATHER)
    time.sleep(2)
    WEATHERSERVICE.notify(WeatherType.WINDY)
    time.sleep(2)
    WEATHERSERVICE.notify(WeatherType.COLD)
