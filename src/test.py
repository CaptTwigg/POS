import os
import sys
import time

from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, \
    QPushButton

from MainController import MainController
from Menu import Menu


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Main")
        self.initUI()

    def initUI(self):
        widget = QWidget()
        widgetB = QWidget()
        widgetBLay = QVBoxLayout()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(QPushButton("button"), 0, 0)
        self.layout.addWidget(QPushButton("button"), 0, 1)
        self.layout.addWidget(QPushButton("button"), 0, 2)
        self.layout.addWidget(QPushButton("button"), 1, 0)
        self.layout.addWidget(QPushButton("button"), 1, 2)

        menu = Menu()
        widget.setStyleSheet("background: blue")
        self.layout.addWidget(menu, 0,3)

        widgetB.setLayout(self.layout)
        widgetB.setStyleSheet("background : red")
        widgetBLay.addWidget(widgetB)
        widget.setLayout(widgetBLay)

        self.setCentralWidget(widget)
        self.setWindowTitle("POS")
        FG = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        FG.moveCenter(cp)
        self.move(FG.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())
