import sys
import time

from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QStyleOption, QStyle

from Menu import Menu
from MenuTab import MenuTab
from Purchase import Purchase
from Tabs import Tabs


class MainController(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setObjectName("MainController")

        self.mainWindow = mainWindow

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(Tabs(), 0, 0)
        self.layout.addWidget(Menu(), 0, 1)
        self.layout.addWidget(Purchase(), 0, 2)

        self.setLayout(self.layout)

        self.styleFile = "../resources/style.css"
        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(self.styleFile)
        self.watcher.fileChanged.connect(self.updateStyleSheet)
        self.updateStyleSheet()

    def updateStyleSheet(self):
        print("Update Style")
        time.sleep(.2)
        with open(self.styleFile, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
            self.mainWindow.setStyleSheet(style)
        self.watcher.addPath(self.styleFile)

    def paintEvent(self, event):
        "Reimplementation of paintEvent to allow for style sheets"
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainController()
    ex.show()
    sys.exit(app.exec_())
