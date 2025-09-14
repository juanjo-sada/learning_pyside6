import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedLayout
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("QStackedLayout")
        layout = QStackedLayout()
        layout.addWidget(Color("Red"))
        layout.addWidget(Color("Blue"))
        layout.addWidget(Color("Yellow"))
        layout.addWidget(Color("Green"))

        layout.setCurrentIndex(1) # Index shows in the order you added the widget

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()