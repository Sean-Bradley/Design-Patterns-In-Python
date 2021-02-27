"A Director Class"
from house_builder import HouseBuilder


class CastleDirector:  # pylint: disable=too-few-public-methods
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return HouseBuilder()\
            .set_building_type("Castle")\
            .set_wall_material("Sandstone")\
            .set_number_doors(100)\
            .set_number_windows(200)\
            .get_result()
