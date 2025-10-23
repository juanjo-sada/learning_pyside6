# You can download the SQLite db from here:
# https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite
import os, sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
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
        
        # Instead of setting a table and calling self.model.select(), we define an SQL Query
        query = QSqlQuery("SELECT Name, Composer FROM Track as t WHERE t.Name LIKE 'A%'", db=self.db)

        # And then set the query to the model
        self.model.setQuery(query)

        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()