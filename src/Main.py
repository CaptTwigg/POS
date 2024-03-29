import os
import sys
import time

from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QWidget, QLabel, QAction

from MainController import MainController


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Main")
        self.initUI()

    def initUI(self):
        self.setCentralWidget(MainController(self))
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
