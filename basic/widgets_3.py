import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Checkbox")

        checkbox = QCheckBox("This is a checkbox")
        checkbox.setCheckState(Qt.PartiallyChecked)

        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print(f"State is: {state}")
        print(state == Qt.Checked)

app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()