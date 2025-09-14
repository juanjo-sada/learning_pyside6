import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("QTabWidget")

        tabs = QTabWidget()
        # tabs.setTabPosition(QTabWidget.West) # Can use this to place on different parts of the screen, default = North (top)
        # tabs.setMovable(True) # Defines if you can manually change the order of the buttons from the GUI

        for color in ["Red", "Green", "Blue", "Yellow"]:
            tabs.addTab(Color(color), f"Label: {color}") # addTab(QWidget, button label)
        
        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()