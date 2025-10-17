import sys
from datetime import datetime
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.BackgroundRole:
            if index.column() == 0:
                return QtGui.QColor(Qt.blue)
            if index.column() == 1:
                return QtGui.QColor(Qt.red)
            if index.column() == 2:
                return QtGui.QColor(Qt.green)

        # To align text, we check Qt.TextAlignmentRole
        if role == Qt.TextAlignmentRole:
            # Alignment can be done based on data type
            # For example, we can align numbers to the right
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

        data = [
            ["Some value", 12, 13, 14],
            [25.1212312412, 22, 23, 24],
            [datetime(day=13, month=12, year=2025), 32, 33, 34]
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()