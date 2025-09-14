import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Changing Stacked Layout Widget with Buttons")

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)
        
        btn = QPushButton("Red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("Red"))

        btn = QPushButton("Yellow")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("Yellow"))

        btn = QPushButton("Blue")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("Blue"))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stack_layout.setCurrentIndex(2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()