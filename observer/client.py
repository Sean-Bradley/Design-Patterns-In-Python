"Observer Design Pattern Concept"

from data_model import DataModel
from data_controller import DataController
from pie_graph_view import PieGraphView
from bar_graph_view import BarGraphView
from table_view import TableView

# A local data view that the hypothetical external controller updates
DATA_MODEL = DataModel()

# Add some visualisation that use the dataview
PIE_GRAPH_VIEW = PieGraphView(DATA_MODEL)
BAR_GRAPH_VIEW = BarGraphView(DATA_MODEL)
TABLE_VIEW = TableView(DATA_MODEL)


# A hypothetical data controller running in a different process
DATA_CONTROLLER = DataController()

# The hypothetical external data controller updates some data
DATA_CONTROLLER.notify([1, 2, 3])

# Client now removes a local BAR_GRAPH
BAR_GRAPH_VIEW.delete()

# The hypothetical external data controller updates the data again
DATA_CONTROLLER.notify([4, 5, 6])
