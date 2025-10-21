import os, sys, re

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QTableView, 
    QWidget, 
    QLineEdit, 
    QPushButton, 
    QLabel, 
    QVBoxLayout
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(basedir, 'chinook.sqlite'))
        self.db.open()

        # Create container widget and layout
        container = QWidget()
        layout = QVBoxLayout()

        # Create label, Line Edit, button and the table
        self.label = QLabel("Filter 'Name' Column")
        self.edit = QLineEdit()
        self.button = QPushButton("Apply Filter")
        self.table = QTableView()

        # Connect the button press to the update filter method
        self.button.pressed.connect(self.update_filter)
        
        # Add all widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.table)
        container.setLayout(layout)

        # Create the Table Model and set it
        self.model = QSqlTableModel(db=self.db)
        self.table.setModel(self.model)

        # Select the table to use
        self.model.setTable("Track")
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(container)

    def update_filter(self):
        """
        Triggered by self.button
        - Takes the text from the line edit, 
        - Removes any characters that aren't alphanumeric
        - Applies a filter where the 'Name' column contains the text values
        """
        text = self.edit.text()
        clean_text = re.sub("[\W_]+", '', text)
        filter_str = 'Name LIKE "%{}%"'.format(clean_text)
        self.model.setFilter(filter_str)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()