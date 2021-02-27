"The Factory Class"
from small_table import SmallTable
from medium_table import MediumTable
from big_table import BigTable


class TableFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_table(table):
        "A static method to get a table"
        try:
            if table == 'BigTable':
                return BigTable()
            if table == 'MediumTable':
                return MediumTable()
            if table == 'SmallTable':
                return SmallTable()
            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)
        return None
