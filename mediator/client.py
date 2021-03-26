"The Mediator Use Case Example"
from component import Component
from mediator import Mediator

MEDIATOR = Mediator()
COMPONENT1 = Component(MEDIATOR, "Component1")
COMPONENT2 = Component(MEDIATOR, "Component2")
COMPONENT3 = Component(MEDIATOR, "Component3")
MEDIATOR.add(COMPONENT1)
MEDIATOR.add(COMPONENT2)
MEDIATOR.add(COMPONENT3)

COMPONENT1.notify("data A")
COMPONENT2.notify("data B")
COMPONENT3.notify("data C")
