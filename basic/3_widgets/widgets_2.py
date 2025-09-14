import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
)

basedir = os.path.dirname(os.path.dirname(__file__))
print(f"Current working folder: {os.getcwd()}")
print(f"Paths are relative to: {basedir}")

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Bird picture")

        bird_path = os.path.join(os.path.dirname(basedir), "pictures", "bird.jpg")

        widget = QLabel()
        widget.setPixmap(QPixmap(bird_path)) # Set the label to a Pixelmap (the picture)
        widget.setScaledContents(True) # Allow for the contents to be scaled when resizing the window

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()