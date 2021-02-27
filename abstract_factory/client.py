"Abstract Factory Use Case Example Code"
from furniture_factory import FurnitureFactory


FURNITURE = FurnitureFactory.get_furniture("SmallChair")
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("MediumTable")
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")
