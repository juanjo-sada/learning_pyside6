import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Nested-list data structure
            # index.row() indexes into outer list
            # index.column() indexes into inner list
            return self._data[index.row()][index.column()]
    
    def rowCount(self, index):
        # Returns length of the outer list
        return len(self._data)

    def columnCount(self, index):
        # Returns length of inner list of the first sub-list
        # Only works if all rows are same length
        return len(self._data[0])
    

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [11, 12, 13, 14, 15],
            [21, 22, 23, 24, 25],
            [31, 32, 33, 34, 35]
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()