import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Toolbars")

        label = QLabel("Toolbar Example")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar") # Create a QToolBar instance
        self.addToolBar(toolbar) # Add instance to the main window


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()