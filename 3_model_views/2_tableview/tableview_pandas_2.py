from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import pandas as pd
import os

basedir = os.path.dirname(__file__)
datadir = os.path.join(basedir, 'data')

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data if data else pd.DataFrame()

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

        self.data_path = os.path.join(datadir, 'data.csv')
        self.table = QtWidgets.QTableView()
        
        self.model = TableModel()

        self.load()

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

        self.setGeometry(600, 100, 400, 200)

        self.save()

    def load(self):
        try:
            self.model._data = pd.read_csv(self.data_path, index_col=0)
        except Exception as e:
            print(f"Found error: {e}")

    def save(self):
        self.model._data.to_csv(self.data_path)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()