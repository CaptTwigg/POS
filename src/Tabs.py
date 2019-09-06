from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout, QBoxLayout, QPushButton, QHBoxLayout, QWidget, QStyleOption, QStyle


class Tabs(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Tabs")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        #self.layout.ali
        tabs = [
                QPushButton("Food"),
                QPushButton("Drinks"),
                QPushButton("Dessert"),
        ]
        for button in tabs:
            self.layout.addWidget(button)
    def paintEvent(self, event):
        "Reimplementation of paintEvent to allow for style sheets"
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()