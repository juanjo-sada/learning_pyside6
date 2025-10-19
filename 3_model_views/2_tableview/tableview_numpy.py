from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import numpy as np


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # use data[row, col] instead of data[row][col] now that we're using numpy
            # data needs for us to return int, float, or str, but numpy has it's own datatypes, so we need to convert first
            return str(self._data[index.row(), index.column()])
    
    def rowCount(self, index):
        # Access shape[0] to get row count
        return self._data.shape[0]

    def columnCount(self, index):
        # Access shape[1] to get column count
        return self._data.shape[1]
    

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        # Create data as numpy array
        data = np.array(
            [
                [1, 9, 2],
                [1, 0 , -1],
                [2, 6, 9],
                [3, 3, 2]
            ]
        )

        self.model = TableModel(data)

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

        self.setGeometry(600, 100, 400, 200)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()