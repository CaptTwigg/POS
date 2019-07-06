from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QVBoxLayout


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


        self.layout.addWidget(QPushButton("button"), 0, 0)
        self.layout.addWidget(QPushButton("button"), 0, 1)
        self.layout.addWidget(QPushButton("button"), 0, 2)
        self.layout.addWidget(QPushButton("button"), 1, 0)
        self.layout.addWidget(QPushButton("button"), 1, 2)

