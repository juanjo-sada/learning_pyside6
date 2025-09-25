import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QDialog
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs 1")

        button = QPushButton("Open dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Button clicked, opening dialog")

        dialog = QDialog(self)
        dialog.setWindowTitle("?")
        dialog.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()