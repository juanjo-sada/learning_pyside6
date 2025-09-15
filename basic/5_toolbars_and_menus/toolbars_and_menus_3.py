import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel,
    QStatusBar
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Toolbars")

        label = QLabel("Toolbar Example")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.on_my_toolbar_button_click)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def on_my_toolbar_button_click(self):
        print(f"Clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()