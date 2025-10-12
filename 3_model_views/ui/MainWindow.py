# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(253, 330)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todoView = QListView(self.centralwidget)
        self.todoView.setObjectName(u"todoView")

        self.verticalLayout.addWidget(self.todoView)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.completeButton = QPushButton(self.frame)
        self.completeButton.setObjectName(u"completeButton")

        self.horizontalLayout.addWidget(self.completeButton)


        self.verticalLayout.addWidget(self.frame)

        self.todoEdit = QLineEdit(self.centralwidget)
        self.todoEdit.setObjectName(u"todoEdit")

        self.verticalLayout.addWidget(self.todoEdit)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 253, 33))
        self.menuTo_Do_App = QMenu(self.menubar)
        self.menuTo_Do_App.setObjectName(u"menuTo_Do_App")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuTo_Do_App.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.completeButton.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add To Do", None))
        self.menuTo_Do_App.setTitle(QCoreApplication.translate("MainWindow", u"To Do App", None))
    # retranslateUi

