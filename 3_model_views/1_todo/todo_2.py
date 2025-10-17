import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QAbstractListModel

from ui.MainWindow import Ui_MainWindow


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos if todos else []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text
        
    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Initialize main window and setup the UI
        super().__init__()
        self.setupUi(self)

        # Create the custom QAbstractListModel and assign it to self.model
        self.model = TodoModel(todos=[(False, "My First Todo")])
        # Set the model of the QListWidget to self.model
        self.todoView.setModel(self.model)
        # Connect to the slot created to add the new todo
        self.addButton.pressed.connect(self.add)

    def add(self):
        # Get the text from the QLineEdit which
        text = self.todoEdit.text()
        # Ensure we got something back
        if text:
            # Strip to avoid trailing and leading whitespaces
            text = text.strip()
            # Append the new todo as false
            self.model.todos.append((False, text))
            # We emit the signal to let the view know that we have updated the
            # data, if we don't do this step, the todo will still be added to
            # the list, but the view will not display the change.
            self.model.layoutChanged.emit()
            # Reset the text of the QLineEdit
            self.todoEdit.setText("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()