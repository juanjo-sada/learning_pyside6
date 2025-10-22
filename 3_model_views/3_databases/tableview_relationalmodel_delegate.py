import os, sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelationalDelegate, QSqlRelation
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(basedir, 'chinook.sqlite'))
        self.db.open()

        self.table = QTableView()

        self.model = QSqlRelationalTableModel(db=self.db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        self.model.setRelation(
            2, QSqlRelation("Album", "AlbumId", "Title")
        )
        self.model.setRelation(
            3, QSqlRelation("MediaType", "MediaTypeId", "Name")
        )
        self.model.setRelation(
            4, QSqlRelation("Genre", "GenreId", "Name")
        )

        # We can use a relational delegate to show a QComboBox of the items in the related table
        delegate = QSqlRelationalDelegate(self.table)
        self.table.setItemDelegate(delegate)
        
        self.model.select()

        self.model.setEditStrategy(QSqlRelationalTableModel.OnRowChange)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()