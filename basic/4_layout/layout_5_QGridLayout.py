import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("QGridLayout")
        layout = QGridLayout()
        layout.addWidget(Color("Red"), 0, 0)
        layout.addWidget(Color("Blue"), 1, 0)
        layout.addWidget(Color("Yellow"), 1, 1)
        layout.addWidget(Color("Green"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()