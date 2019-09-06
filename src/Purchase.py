import sys

from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QApplication, QStyle, \
    QStyleOption


class Purchase(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("purchaseView")
        # self.setStyleSheet("background-color: blue")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # button
        ######
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setPlaceholderText("0")
        self.display.setAlignment(Qt.AlignRight)
        self.display.setValidator(QDoubleValidator())

        self.numbers = [QPushButton(str(i)) for i in range(10)]
        for num in self.numbers:
            num.pressed.connect(lambda text=num.text(): self.appendToDisplay(text))

        self.delete = QPushButton("&C")
        self.delete.pressed.connect(self.clearDisplay)

        self.multiply = QPushButton("X")
        self.multiply.pressed.connect(lambda: self.appendToDisplay("*"))

        self.enter = QPushButton("Enter")
        self.enter.setObjectName("Enter")
        self.enter.pressed.connect(self.calculateDisplay)
        self.enter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.dot = QPushButton(".")
        self.dot.pressed.connect(lambda: self.appendToDisplay(self.dot.text()))

        self.minus = QPushButton("-")
        self.minus.pressed.connect(lambda: self.appendToDisplay(self.minus.text()))

        ######

        # Layout
        self.layout.addWidget(self.display, 0, 0, 1, 5)

        self.layout.addWidget(self.numbers[7], 1, 0)
        self.layout.addWidget(self.numbers[8], 1, 1)
        self.layout.addWidget(self.numbers[9], 1, 2)
        self.layout.addWidget(self.delete, 1, 3, 1, 2)

        self.layout.addWidget(self.numbers[4], 2, 0)
        self.layout.addWidget(self.numbers[5], 2, 1)
        self.layout.addWidget(self.numbers[6], 2, 2)
        self.layout.addWidget(self.multiply, 2, 3, 1, 2)

        self.layout.addWidget(self.numbers[1], 3, 0)
        self.layout.addWidget(self.numbers[2], 3, 1)
        self.layout.addWidget(self.numbers[3], 3, 2)
        self.layout.addWidget(self.enter, 3, 3, 2, 2)

        self.layout.addWidget(self.numbers[0], 4, 0)
        self.layout.addWidget(self.dot, 4, 1)
        self.layout.addWidget(self.minus, 4, 2)

    def appendToDisplay(self, text):
        self.display.setText(self.display.text() + text)

    def clearDisplay(self):
        self.display.clear()

    def calculateDisplay(self):
        if self.display.text():
            try:
                result = eval(self.display.text())
                self.display.setText(f"{result:.2f}")
            except Exception as e:
                print("Calculation not possible")
                print(e)

    def paintEvent(self, event):
        "Reimplementation of paintEvent to allow for style sheets"
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Purchase()
    ex.show()
    sys.exit(app.exec_())
