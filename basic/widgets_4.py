import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("ComboBox")

        combo = QComboBox()
        combo.addItems(["First", "Second", "Third"])

        combo.currentIndexChanged.connect(self.index_changed)
        combo.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(combo)

    def index_changed(self, index):
        print("New index:", index)

    def text_changed(self, text):
        print("New text: ", text)


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()