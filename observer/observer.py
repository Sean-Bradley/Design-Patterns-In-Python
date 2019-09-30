"""
Observer Design Pattern
"""

from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """The subscribe method"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """The unsubscribe method"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """The notify method"""


class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """Receive notifications"""


class Observer(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Observer received", args, kwargs)


SUBJECT = Subject()
OBSERVERA = Observer(SUBJECT)
OBSERVERB = Observer(SUBJECT)

SUBJECT.notify("Hello Observers")

SUBJECT.unsubscribe(OBSERVERB)
SUBJECT.notify("Hello Observers")
