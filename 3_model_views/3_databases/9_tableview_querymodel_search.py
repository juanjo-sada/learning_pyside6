# You can download the SQLite db from here:
# https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite
import os, sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QHeaderView
)

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ---- Setup Database ----
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(basedir, 'chinook.sqlite'))
        if not self.db.open():
            print("Unable to open database")
            return

        # ---- Setup search components ----
        container_search = QWidget()
        layout_search = QHBoxLayout()

        self.track_search = QLineEdit()
        self.composer_search = QLineEdit()
        self.album_search = QLineEdit()

        search_components = [
            {
                "label": "Filter Track",
                "search": self.track_search
            },
            {
                "label": "Filter Composer",
                "search": self.composer_search
            },
            {
                "label": "Filter Album",
                "search": self.album_search
            }
        ]

        for search_component in search_components:
            label = search_component.get('label')
            search = search_component.get('search')
            box = QWidget()
            vlayout = QVBoxLayout()
            vlayout.addWidget(QLabel(label))
            vlayout.addWidget(search)
            box.setLayout(vlayout)
            layout_search.addWidget(box)
        
        container_search.setLayout(layout_search)

        # ---- Table View ----
        self.table = QTableView()

        layout = QVBoxLayout()
        layout.addWidget(container_search)
        layout.addWidget(self.table)

        # ---- Central Container ----
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # ---- Model ----
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)
        # Use this line to stretch the table to fit the whole widget
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # ---- Query ----
        self.query = QSqlQuery(db = self.db)
        # Select 3 columns, and place parameters to be replaced by update_query slot
        self.query.prepare(
            "SELECT Name, Composer, Album.Title FROM Track "
            "INNER JOIN Album on Track.AlbumId=Album.AlbumId WHERE "
            "Track.Name LIKE '%' || :track_name || '%' AND "
            "Track.Composer LIKE '%' || :track_composer || '%' AND "
            "Album.Title LIKE '%' || :track_album || '%' "
        )
        self.update_query()

        # ---- Signals ----
        self.track_search.textChanged.connect(self.update_query)
        self.composer_search.textChanged.connect(self.update_query)
        self.album_search.textChanged.connect(self.update_query)
        
        # ---- Window settings ----
        self.setWindowTitle("Chinook Database Viewer")
        self.setMinimumSize(QSize(1024, 600))

    def update_query(self, s=None):
        """
        Binds the text on each QLineEdit to the query and executes it
        """
        self.query.bindValue(":track_name", self.track_search.text())
        self.query.bindValue(":track_composer", self.composer_search.text())
        self.query.bindValue(":track_album", self.album_search.text())
        self.query.exec()
        self.model.setQuery(self.query)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()