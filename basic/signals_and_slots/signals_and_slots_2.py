import sys
from random import choice # importing choice to randomly select a window title

from PySide6.QtCore import QSize # Importing QSize to set a fixed size on our window
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

# List of possible window titles
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
        self.windowTitleChanged.connect(self.window_title_changed) # Add a signal for when the window title changes

        self.setCentralWidget(self.button_main)

    def button_was_clicked(self):
        print("Button was clicked")
        # When the button is clicked, select a new window title at random from the list
        new_window_title = choice(possible_window_titles)
        print(f"Setting new window title: {new_window_title}")
        # Set the new window title
        self.setWindowTitle(new_window_title)

    def window_title_changed(self, window_title):
        print(f"Window title has changed to {window_title}")
        # check if the window title was changed to "Error"
        if window_title == "Error":
            print("Ran into an error, disabling the button")
            # Disable the button if the new title is "Error"
            self.button_main.setEnabled(False)
        


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()