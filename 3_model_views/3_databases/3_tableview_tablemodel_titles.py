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

        # You can change the header names
        # Use the index, Qt.Horizontal to refer to a top header (column), and the new label
        self.model.setHeaderData(2, Qt.Horizontal, "Album (ID)")

        # You can also make the change based on the column name by finding the index first
        column_changes = {
            "MediaTypeId": "Media Type (ID)",
            "GenreId": "Genre (ID)",
        }
        for original_col_name, new_col_name in column_changes.items():
            index = self.model.fieldIndex(original_col_name)
            self.model.setHeaderData(index, Qt.Horizontal, new_col_name)

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()