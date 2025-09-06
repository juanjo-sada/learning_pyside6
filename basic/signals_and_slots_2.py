import sys
from random import choice

from PySide6.QtCore import QSize # Importing QSize to set a fixed size on our window
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

possible_window_titles = [
    "Title 1",
    "Title 2",
    "Title 3",
    "Title 4",
    "Title 5",
    "Error"
]

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Main Window")

        self.button_main = QPushButton("Main Button")
        self.button_main.clicked.connect(self.button_was_clicked)
        self.windowTitleChanged.connect(self.window_title_changed)

        self.setCentralWidget(self.button_main)

    def button_was_clicked(self):
        print("Button was clicked")
        self.setWindowTitle(choice(possible_window_titles))
        if self.windowTitle == "Error":
            self.button_main.setText("Ran into an error, disabling this")
            self.button_main.setEnabled(False)

    def window_title_changed(self, window_title):
        print(f"Window title has changed to {window_title}")
        if window_title == "Error":
            self.button_main.setText("Ran into an error, disabling this button")
            self.button_main.setEnabled(False)
        


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()