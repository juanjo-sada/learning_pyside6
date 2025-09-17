import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QInputDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Integer Input")

        layout = QVBoxLayout()

        # Add button to get an integer
        button1 = QPushButton("Request an Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)

        # Add button to request a float
        button2 = QPushButton("Request a Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        # Add button to show a dropdown list and give user to select an option
        button3 = QPushButton("Pick a string from a list")
        button3.clicked.connect(self.get_a_str_from_a_list)
        layout.addWidget(button3)

        # Add button to request a password
        button4 = QPushButton("Request a password")
        button4.clicked.connect(self.get_text)
        layout.addWidget(button4)

        # Add button to request multiline text
        button5 = QPushButton("Request multiline text")
        button5.clicked.connect(self.get_multiline_text)
        layout.addWidget(button5)

        # Create a widget to be the main container
        container = QWidget()
        # Set layout containing the buttons declared above
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_an_int(self):
        """
        Use QInputDialog.getInt() to request an integer
        """
        title = "Get an integer"
        label = "Enter a number"
        int_value, ok = QInputDialog.getInt(
            self,
            title,
            label,
            value=0,
            minValue=-10,
            maxValue=10,
            step=5,
        )
        print("Result:", ok, int_value)

    def get_a_float(self):
        """
        Use QInputDialog.getDouble() to request an float
        """
        title = "Get a float"
        label = "Enter a number"
        float_value, ok = QInputDialog.getDouble(
            self,
            title,
            label,
            value=0,
            minValue=-100.5,
            maxValue=100.5,
            step=5
        )
        print("Result:", ok, float_value)

    def get_a_str_from_a_list(self):
        """
        Use QInputDialog.getItem() to show a dropdown of a given list, have the user select one, and return the selection
        """
        title = "Select a string"
        label = "Select a fruit from the list"
        items = ["Apple", "Pear", "Orange"]
        initial_selection = 0
        selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            editable=False
        )
        print("Result:", ok, selected_str)
        
    def get_text(self):
        """
        Use QInputDialog.getText() to request a string from the user
        Using QLineEdit.Password mode to set input as asterisks
        """
        title = "Enter text"
        label = "Type your password"
        mode = QLineEdit.Password
        placeholder = "Your password here"
        input_text, ok = QInputDialog.getText(
            self, title, label, mode
        )
        print("Result:", ok, input_text)

    def get_multiline_text(self):
        """
        User QInputDialog.getMultiLineText() to request multiline text from the user
        User multiline_text.split("\n") to return a list of one item per row
        """
        title = "Enter multiline text"
        label = "Enter your multiline text here"
        placeholder = ""
        multiline_text, ok = QInputDialog.getMultiLineText(
            self, title, label, placeholder
        )
        print("Result:", ok, multiline_text)
        print(multiline_text.split("\n"))



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()