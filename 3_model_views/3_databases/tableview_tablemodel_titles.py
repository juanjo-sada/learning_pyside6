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

        index = self.model.fieldIndex("Milliseconds")
        self.model.setSort(index, Qt.DescendingOrder)

        # You can change the header names
        # Use the index, Qt.Horizontal to refer to a top header (column), and the new label
        self.model.setHeaderData(2, Qt.Horizontal, "Album (ID)")
        self.model.setHeaderData(3, Qt.Horizontal, "Media Type (ID)")
        self.model.setHeaderData(4, Qt.Horizontal, "Genre (ID)")

        self.model.select()

        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()