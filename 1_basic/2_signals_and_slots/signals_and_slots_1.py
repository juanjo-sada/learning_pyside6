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
        
        self.setWindowTitle("Main Window")

        self.button_main = QPushButton("Main Button")
        self.button_main.clicked.connect(self.button_was_clicked)

        self.setCentralWidget(self.button_main)

    def button_was_clicked(self):
        self.button_main.setText("You clicked me, you can't undo it anymore")
        self.button_main.setEnabled(False)
        self.setWindowTitle("They have clicked the button")


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()