# You can download the SQLite db from here:
# https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite
import os, sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the db to q SQLite database
        self.db = QSqlDatabase("QSQLITE")
        # Select the db from the same directory as this file
        self.db.setDatabaseName(os.path.join(basedir, 'chinook.sqlite'))
        # Open the db
        self.db.open()

        self.table = QTableView()

        # Create a Table Model using the db
        self.model = QSqlTableModel(db=self.db)

        self.table.setModel(self.model)

        # Choose what table to work with from the db. Our model only allows for a single table
        # For working with multiple tables, use the QSqlRelationalTableModel
        self.model.setTable("Track")
        self.model.select()

        # Set the editing strategy, this defines what triggers the changes made to be saved to the db
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()