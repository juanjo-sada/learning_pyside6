from PySide6.QtWidgets import QApplication, QWidget

import sys

# Main application, only needs to be one
app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()