"Factory Use Case Example Code"

from chair_factory import ChairFactory

# The Client
CHAIR = ChairFactory().get_chair("SmallChair")
print(CHAIR.get_dimensions())
