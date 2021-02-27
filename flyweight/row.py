"A Row in the Table"
from column import Column


class Row():  # pylint: disable=too-few-public-methods
    "A Row in the Table"

    def __init__(self, column_count: int) -> None:
        self.columns = []
        for _ in range(column_count):
            self.columns.append(Column())

    def get_data(self):
        "Format the row before returning it to the table"
        ret = ""
        for column in self.columns:
            ret = f"{ret}{column.get_data()}|"
        return ret
