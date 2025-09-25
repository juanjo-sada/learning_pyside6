import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextBrowser
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Events 1")
        self.setCentralWidget(self.label)

        def mouseMoveEvent(self, e):
            if e.button() == Qt.leftButton:
                print("mouseMoveEvent LEFT")
    
        def mousePressEvent(self, e):
            self.label.setText("mousePressEvent")
    
        def mouseReleaseEvent(self, e):
            self.label.setText("mouseReleaseEvent")
    
        def mouseDoubleClickEvent(self, e):
            self.label.setText("mouseDoubleClickEvent")
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()