import sys, os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel,
    QStatusBar,
    QCheckBox
)

basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Toolbars")

        label = QLabel("Toolbar Example")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basedir, 'icons', 'bug.png')),
            "Your button",
            self
        )

        button_action.setCheckable(True)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.on_my_toolbar_button_click)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Hello"))

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar() # Added a menuBar

        file_menu = menu.addMenu("&File") # Added a 'File' menu
        file_menu.addAction(button_action) # Added the action we already had before

    def on_my_toolbar_button_click(self, checked):
        print(f"Checked: {checked}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()