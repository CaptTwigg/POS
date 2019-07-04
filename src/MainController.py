import time

from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtWidgets import QWidget, QGridLayout

from Purchase import Purchase


class MainController(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = QGridLayout()
        self.layout.addWidget(Purchase(), 0, 0)



        self.setLayout(self.layout)

        self.styleFile = "../resources/style.css"
        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(self.styleFile)
        self.watcher.fileChanged.connect(self.updateStyleSheet)
        self.updateStyleSheet()

        for i in self.children():
            print(i.objectName())



    def updateStyleSheet(self):
        print("Update Style")
        time.sleep(.2)
        with open(self.styleFile, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
            self.mainWindow.setStyleSheet(style)
        self.watcher.addPath(self.styleFile)
