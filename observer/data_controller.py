"A Data Conroller which is a Subject"
from interface_data_controller import IDataController


class DataController(IDataController):
    "A Subject (a.k.a Observable)"

    _instance = None
    _observers = set()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = DataController
        return cls._instance

    @classmethod
    def subscribe(cls, observer):
        cls._observers.add(observer)

    @classmethod
    def unsubscribe(cls, observer):
        cls._observers.remove(observer)

    @classmethod
    def notify(cls, *args):
        for observer in cls._observers:
            observer.notify(*args)
