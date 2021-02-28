"A Data Model that observes the Data Controller"
from interface_data_model import IDataModel
from data_controller import DataController


class DataModel(IDataModel):
    "A Subject (a.k.a Observable)"

    def __init__(self):
        self._observers = {}
        self._counter = 0
        # subscribing to an external hypothetical data controller
        self._data_controller = DataController()
        self._data_controller.subscribe(self)

    def subscribe(self, observer):
        self._counter = self._counter + 1
        self._observers[self._counter] = observer
        return self._counter

    def unsubscribe(self, observer_id):
        self._observers.pop(observer_id)

    def notify(self, data):
        for observer in self._observers:
            self._observers[observer].notify(data)
