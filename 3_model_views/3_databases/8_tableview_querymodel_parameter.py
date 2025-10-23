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

        # We create a blank query so we can prepare it
        query = QSqlQuery(db=self.db)
        # We prepare a query giving a parameter to be binded later
        # We're setting the parameter :album_title between LIKE %{}% to execute a 'contains' query
        # Note the extra spaces at the end of each line so they are there when we concatenate
        query.prepare(
            "SELECT Name, Composer, Album.Title as 'Album Title' FROM TRACK "
            "INNER JOIN Album ON Track.AlbumId = Album.AlbumId "
            "WHERE Album.Title LIKE '%' || :album_title || '%' "
        )
        # We bing (replace) the parameter with the value to search for
        query.bindValue(":album_title", "Sinatra")
        # We execute the query
        query.exec()

        self.model.setQuery(query)
        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()