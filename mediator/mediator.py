"The Subject that all components will stay synchronized with"


class Mediator():
    "A Subject whose notify method is mediated"

    def __init__(self):
        self._components = set()

    def add(self, component):
        "Add components"
        self._components.add(component)

    def notify(self, message, originator):
        "Add components except for the originator component"
        for component in self._components:
            if component != originator:
                component.receive(message)
