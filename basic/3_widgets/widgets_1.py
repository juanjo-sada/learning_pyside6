import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Widgets 1")

        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        ## Horizontal alignment
        # Qt.AlignLeft
        # Qt.AlignRight
        # Qt.AlignHCenter
        # Qt.AlignJustify

        ## Vertical Alignment
        # Qt.AlignTop
        # Qt.AlignBottom
        # Qt.AlignVCenter

        ## Align center horizontally and vertically
        # Qt.AlignCenter

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()