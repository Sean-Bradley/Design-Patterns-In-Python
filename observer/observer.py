from abc import ABCMeta, abstractstaticmethod
from enum import Enum
import time


class WeatherType(Enum):
    SUNNY = 1
    RAINY = 2
    WINDY = 3
    COLD = 4


class Weather():
    """Observable"""

    def __init__(self):
        self._observers = set()
        pass

    def register(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self, weather_type):
        for observer in self._observers:
            observer.update(weather_type)


class IObserver(metaclass=ABCMeta):

    @abstractstaticmethod
    def update(WeatherType):
        """Update all the registered observers"""


class BBCWeather(IObserver):
    def __init__(self, observable):
        observable.register(self)

    def update(self, weather_type):
        print(f"{__class__} : {repr(weather_type)}")


class ABCWeather(IObserver):
    def __init__(self, observable):
        observable.register(self)

    def update(self, weather_type):
        print(f"{__class__} : {repr(weather_type)}")


class NBCWeather(IObserver):
    def __init__(self, observable):
        observable.register(self)

    def update(self, weather_type):
        print(f"{__class__} : {repr(weather_type)}")


if __name__ == "__main__":

    WEATHERSERVICE = Weather()

    BBCWEATHER = BBCWeather(WEATHERSERVICE)
    ABCWEATHER = ABCWeather(WEATHERSERVICE)
    NBCWEATHER = NBCWeather(WEATHERSERVICE)

    WEATHERSERVICE.notify(WeatherType.RAINY)
    WEATHERSERVICE.remove_observer(BBCWEATHER)
    time.sleep(2)
    WEATHERSERVICE.notify(WeatherType.SUNNY)
    WEATHERSERVICE.remove_observer(NBCWEATHER)
    time.sleep(2)
    WEATHERSERVICE.notify(WeatherType.WINDY)
    time.sleep(2)
    WEATHERSERVICE.notify(WeatherType.COLD)
