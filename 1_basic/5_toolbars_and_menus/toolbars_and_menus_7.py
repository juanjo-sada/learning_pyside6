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
        # Create window and set size
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("Toolbars")

        # Set label for middle text
        label = QLabel("Toolbar Example")
        label.setAlignment(Qt.AlignCenter)

        # Set label as central widget
        self.setCentralWidget(label)

        # Create and add the toolbar to the window
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Create an action for a button, selecting the icon to use
        button_action = QAction(
            QIcon(os.path.join(basedir, 'icons', 'bug.png')),
            "Bug Button",
            self
        )

        # Create another action for a different button this time
        button_action2 = QAction(
            QIcon(os.path.join(basedir, 'icons', 'car-red.png')),
            "Red Car Button",
            self
        )

        # Set properties and connect the first action to a slot
        button_action.setCheckable(True)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.on_my_toolbar_button_click)

        # Set properties and connect second action to a slot
        button_action2.setStatusTip("This is a red car")
        button_action2.triggered.connect(self.on_car_icon_clicked)

        # Add the action to the toolbar
        toolbar.addAction(button_action)

        # Add a status bar at the bottom of the screen
        self.setStatusBar(QStatusBar(self))

        # Add a menu bar
        menu = self.menuBar()

        # Add the file menu, and the button_action to that meun
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

        # Add a submenu
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def on_my_toolbar_button_click(self, checked):
        print(f"Checked: {checked}")

    def on_car_icon_clicked(self):
        print(f"Clicked red car icon in submenu")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()