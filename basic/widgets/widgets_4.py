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

        combo = QComboBox() # Create Combo Box
        combo.addItems(["First", "Second", "Third"]) # Add items to the Combo Box

        combo.currentIndexChanged.connect(self.index_changed) # Trigger signal when index changes
        combo.currentTextChanged.connect(self.text_changed) # Trigger signal when text changes

        combo.setEditable(True) # Let users add new values to the Box

        self.setCentralWidget(combo)

    # Display new index when changed
    def index_changed(self, index):
        print("New index:", index)

    # Display new text when changed
    def text_changed(self, text):
        print("New text: ", text)


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()