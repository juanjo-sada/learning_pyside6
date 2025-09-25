import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Windows 1")
        # self.second_window = None

        layout = QVBoxLayout()

        self.label = QLabel("Main Window")
        layout.addWidget(self.label)

        self.button = QPushButton("Press to toggle new window")
        self.button.clicked.connect(self.create_new_window)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_new_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Label on Second Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()