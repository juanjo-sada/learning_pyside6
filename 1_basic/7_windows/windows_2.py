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
        self.second_window = SecondWindow()

        layout = QVBoxLayout()

        self.label = QLabel("Main Window")
        layout.addWidget(self.label)

        self.button = QPushButton("Press to toggle new window")
        self.button.clicked.connect(self.toggle_window)
        layout.addWidget(self.button)

        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.second_window.label.setText)
        layout.addWidget(self.line_edit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def toggle_window(self):
        if self.second_window.isVisible():
            self.second_window.hide()
        else:
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