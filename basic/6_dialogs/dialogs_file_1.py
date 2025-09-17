import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog, # Import QFileDialog
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog App")

        button = QPushButton("Open a file")
        button.clicked.connect(self.get_filename)

        self.setCentralWidget(button)

    def get_filename(self):
        """
        User QFileDialog.getOpenFileName to request the user to select a file
        Returns the filepath and the filters selected
        """
        # Define a list of filters
        file_filters = [
            "Text files (*.txt)",
            "Comma Separated Values (*.csv)",
            "All files (*.*)"
        ]
        # Select the initial filter
        initial_filter = file_filters[2]
        # Join the list of filters with the ";;" delimiter
        filters = ";;".join(file_filters)

        print("Initial filter:", initial_filter)
        print("Filters:", filters)

        # Create the FileDialog and set the filter options and default selected filter
        filename, selected_filter = QFileDialog.getOpenFileName(
            self, filter=filters, selectedFilter=initial_filter
        )
        print("Result:", filename, selected_filter)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()