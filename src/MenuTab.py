from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton, QStyleOption, QStyle

from Menu import Menu


class MenuTab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setStyleSheet("QTabWidget{background: blue}")
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Create first tab
        layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        layout.addWidget(Menu())
        self.tab1.setLayout(layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def paintEvent(self, event):
        "Reimplementation of paintEvent to allow for style sheets"
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()