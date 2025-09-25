import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QInputDialog,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Dialog Integer Input")

        button1 = QPushButton("Request Integer")
        button1.clicked.connect(self.get_an_int)

        self.setCentralWidget(button1)

    def get_an_int(self):
        # Use QInputDialog.getInt() to request an integer
        # Returns the value and if it was successful
        int_value, ok = QInputDialog.getInt(
            self, "Get an integer", "Enter a number"
        )
        print("Result:", ok, int_value)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()