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

        # Add the complete slot
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        Add the text in the QLineEdit as a new todo
        Update the QListView with the new data
        """
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
        """
        Delete the selected item from the todo list
        """
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

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            print(self.model.todos[row])
            self.model.todos[row] = (True, text)
            print(self.model.todos[row])

            # Because the shape of the data hasn't changed, we use .dataChanged.emit() instead
            # this takes the top left and bottom right as parameters, in this case it's the same
            self.model.dataChanged.emit(index, index)

            # Clear the selection
            self.todoView.clearSelection()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()