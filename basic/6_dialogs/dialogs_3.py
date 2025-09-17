import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialogs 2")

        layout = QVBoxLayout()

        button = QPushButton("Press me to open a constructed QMessageBox")
        button.clicked.connect(self.button_clicked)

        button2 = QPushButton("Press me to open a quickly made QMessageBox.critical")
        button2.clicked.connect(self.button2_clicked)

        button3 = QPushButton("Press me to open a quickly made QMessageBox.question")
        button3.clicked.connect(self.button3_clicked)

        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Question dialog")
        dialog.setText("Can I ask a question?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Apply)
        # Can also be .Information, .Warning .Critical, .NoIcon, etc.
        dialog.setIcon(QMessageBox.Question)
        button = dialog.exec()

        if button == QMessageBox.Yes:
            print("Yes")
        elif button == QMessageBox.Apply:
            print("Apply")
        else:
            print("No")

    def button2_clicked(self):
        QMessageBox.critical(self, "Critical Box", "This was a critical message box constructed quickly")

    def button3_clicked(self):
        QMessageBox.question(self, "Question Box", "This was a question message box constructed quickly")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()