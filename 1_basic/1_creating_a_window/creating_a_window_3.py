from PySide6.QtWidgets import QApplication, QMainWindow

import sys

app = QApplication(sys.argv)

# We use the main window this time
window = QMainWindow()
window.show()

app.exec()