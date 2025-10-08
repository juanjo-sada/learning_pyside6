import os
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import QUiLoader

basedir = os.path.dirname(__file__)
loader = QUiLoader()

class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load(
            os.path.join(basedir, "ui", "gui_1.ui"), None
        )

        self.ui.setWindowTitle("Loading .ui file into self.ui")
        self.ui.show()


app = QtWidgets.QApplication(sys.argv)
window = MainUI()
app.exec()