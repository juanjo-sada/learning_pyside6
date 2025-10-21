import os, sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(basedir, 'chinook.sqlite'))
        self.db.open()

        self.table = QTableView()

        self.model = QSqlTableModel(db=self.db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        # Sort the table based on the third column, must be done before .select()
        # If you change the sort later, you need to call .select() again
        self.model.setSort(2, Qt.DescendingOrder)

        # You can also use a column name, for that you need to find the index of the name
        # index = self.model.fieldIndex("Milliseconds")
        # self.model.setSort(index, Qt.DescendingOrder)
        self.model.select()

        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()