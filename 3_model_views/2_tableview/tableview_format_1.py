import sys
from datetime import datetime
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        """
        To change the format of the value returned from this, you can
        check the type of the value and format it accordingly
        """
        
        if role == Qt.DisplayRole:
            # Get raw value
            value = self._data[index.row()][index.column()]
            
            # Perform check per type and format when rendering
            if isinstance(value, datetime):
                # Render datetime as YYYY-MM-DD
                return value.strftime(format="%Y-%m-%d")
            
            if isinstance(value, float):
                # Render floats with two decimal points
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value
            
            # Default if none of the above are met
            return value
    
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