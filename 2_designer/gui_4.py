import os
import sys
import random

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from uic.MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        f = self.label.font()
        f.setPointSize(25)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setFont(f)

        self.pushButton.pressed.connect(self.update_label)

    def update_label(self):
        n = random.randint(1, 6)
        self.label.setText(f"Random number: {n}")



app = QApplication(sys.argv)
window = MainWindow()
app.exec()