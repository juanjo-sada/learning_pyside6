import sys

from PySide6.QtCore import QSize # Importing QSize to set a fixed size on our window
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("Main Window")

        button = QPushButton("Main Button")
        button.setCheckable(True)
        button.clicked.connect(self.button_was_clicked)
        button.clicked.connect(self.button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def button_was_clicked(self):
        print("Clicked!")

    def button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(f"Button is checked: {self.button_is_checked}")


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()