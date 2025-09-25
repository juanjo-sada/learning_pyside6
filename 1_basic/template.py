import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Template")

        layout = QVBoxLayout()
        self.label = QLabel("Template")
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()