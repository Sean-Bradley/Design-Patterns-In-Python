# pylint: disable=too-few-public-methods
"Abstract Furniture Factory"
from interface_furniture_factory import IFurnitureFactory
from chair_factory import ChairFactory
from table_factory import TableFactory


class FurnitureFactory(IFurnitureFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def get_furniture(furniture):
        "Static get_factory method"
        try:
            if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
                return ChairFactory().get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
                return TableFactory().get_table(furniture)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
