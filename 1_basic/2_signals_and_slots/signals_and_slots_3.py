import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Line edits and Labels")

        # Create a label
        self.label = QLabel()

        # Create an input QLineEdit
        self.input = QLineEdit()
        # When the QLineEdit is edited, and the signal is triggered, update the label text
        self.input.textChanged.connect(self.label.setText)

        # Create a layout to hold all the components
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        # Create a container to contain the layout
        container = QWidget()
        # Set the layout of the container to the QWidget container we just created
        container.setLayout(layout)

        # Set the container as the central widget
        self.setCentralWidget(container)


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()