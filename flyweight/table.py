"A Formatted Table that includes rows and columns"

from row import Row


class Table():  # pylint: disable=too-few-public-methods
    "A Formatted Table"

    def __init__(self, row_count: int, column_count: int) -> None:
        self.rows = []
        for _ in range(row_count):
            self.rows.append(Row(column_count))

    def draw(self):
        "Draws the table formatted in the console"
        max_row_length = 0
        rows = []
        for row in self.rows:
            row_data = row.get_data()
            rows.append(f"|{row_data}")
            row_length = len(row_data) + 1
            if max_row_length < row_length:
                max_row_length = row_length
        print("-" * max_row_length)
        for row in rows:
            print(row)
        print("-" * max_row_length)
