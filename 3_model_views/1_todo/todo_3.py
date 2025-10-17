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

        # Add the delete slot
        self.deleteButton.pressed.connect(self.delete)

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

    def delete(self):
        # Get the selected indexes from the view
        indexes = self.todoView.selectedIndexes()
        # Confirm at least one is selected
        if indexes:
            # If the view is in single-select mode, there will only be one item in the list
            index = indexes[0]
            # Remove the item
            del self.model.todos[index.row()]
            # Refresh the view
            self.model.layoutChanged.emit()
            # Clear the selection as it is no longer valid
            self.todoView.clearSelection()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()