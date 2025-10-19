from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import pandas as pd


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # use data.iloc[row, col] for pandas DataFrame
            # data needs for us to return int, float, or str, but numpy has it's own datatypes, so we need to convert first
            return str(self._data.iloc[index.row(), index.column()])
    
    def rowCount(self, index):
        # Access shape[0] to get row count
        return self._data.shape[0]

    def columnCount(self, index):
        # Access shape[1] to get column count
        return self._data.shape[1]

    # use this to display the header data of the DataFrame
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            # This displays the column names
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            # This displays the index names if any
            if orientation == Qt.Vertical:
                return str(self._data.index[section])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        # Create data as Pandas DataFrame
        data = pd.DataFrame(
            [
                [1, 9, 2],
                [1, 0 , -1],
                [2, 6, 9],
                [3, 3, 2]
            ],
            # Set column names
            columns = ["A","B","C"],
            # Set names for the index
            index = ["Row 1", "Row 2", "Row 3", "Row 4"]
        )

        self.model = TableModel(data)

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

        self.setGeometry(600, 100, 400, 200)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()