from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Menu")
        widget = QWidget()
        self.layout = QGridLayout()

        widget.setLayout(self.layout)
        lay = QVBoxLayout()
        lay.addWidget(widget)
        self.setLayout(self.layout)

        # Menu buttons
        self.burgerBtn = QPushButton("Burger")
        self.saladBtn = QPushButton("Salad")
        self.drinkBtn = QPushButton("Drinks")

        # Added items

        self.layout.addWidget(self.burgerBtn, 0, 0)
        self.layout.addWidget(self.saladBtn, 1, 0)
        self.layout.addWidget(self.drinkBtn, 2, 0)

       # self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

    def paintEvent(self, event):
        "Reimplementation of paintEvent to allow for style sheets"
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()
