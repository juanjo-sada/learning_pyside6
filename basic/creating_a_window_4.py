import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

# Subclass of QMainWindow to customize the main window
class MainWindow(QMainWindow):
    def __init__(self):
        # 
        super().__init__()

        self.setWindowTitle("Main Window")

        button = QPushButton("Main Button")

        self.setCentralWidget(button)


app = QApplication(sys.argv)

# We use the main window this time
window = MainWindow()
window.show()

app.exec()