import sys
from datetime import datetime
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self.COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']

    def data(self, index, role):
        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)

                # Feels like a heatmap
                # Limit to range -5 and +5, then convert to 0...10
                value = max(value, -5) # Values < -5 become -5
                value = min(value, 5) # Values > 5 become 5

                value = value + 5 # -5 becomes 0, 5 becomes 10

                return QtGui.QColor(self.COLORS[value])
            

        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignVCenter | Qt.AlignRight
        
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            
            if isinstance(value, datetime):
                return value.strftime(format="%Y-%m-%d")
            
            if isinstance(value, float):
                return "%.2f" % value

            if isinstance(value, str):
                return '"%s"' % value
            
            return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        # Change some values in 3rd column to negative to test
        data = [
            [-4, -3, -2, -1],
            [0, 1, 2, 3],
            [4, 5, 6, 7],
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()