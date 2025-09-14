from PySide6.QtWidgets import QApplication, QPushButton

import sys

app = QApplication(sys.argv)

# Main window this time is QPushButton instead of QWidget
window = QPushButton("Push me")
window.show()

app.exec()