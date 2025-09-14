import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("List Widget")

        list_widget = QListWidget() # Create Combo Box
        list_widget.addItems(["First", "Second", "Third"]) # Add items to the Combo Box

        list_widget.currentItemChanged.connect(self.item_changed) # Trigger signal when index changes
        list_widget.currentTextChanged.connect(self.text_changed) # Trigger signal when text changes

        self.setCentralWidget(list_widget)

    # Display new index when changed
    def item_changed(self, item):
        print("New item:", item.text())

    # Display new text when changed
    def text_changed(self, text):
        print("New text:", text)


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()