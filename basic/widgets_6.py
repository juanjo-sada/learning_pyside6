import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Line Edit")

        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(10)
        self.line_edit.setPlaceholderText("Write your input here")

        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textChanged.connect(self.text_changed)

        self.setCentralWidget(self.line_edit)

    def return_pressed(self):
        print("Return pressed")
        self.line_edit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed:", self.line_edit.selectedText())

    def text_changed(self, text):
        print("Text changed:", text)
    

app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()