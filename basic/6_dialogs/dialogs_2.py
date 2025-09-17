import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialogs 2")

        button = QPushButton("Press me to open custom dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        dialog = CustomDialog(self)
        # Different buttons will trigger different things, 'Yes' and 'Ok' will trigger 'Success!', while 'No' and 'Cancel' will go to 'Cancel!'
        if dialog.exec():
            print("Success!")
        else:
            print("Cancel!")


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("CustomDialog")

        # QDialogButton automatically orders these based on a standard, Yes to the left, Cancel to the right, etc
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.Yes | QDialogButtonBox.No

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Some message")
        
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()