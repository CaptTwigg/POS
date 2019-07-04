from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit


class Purchase(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("purchaseView")
        # self.setStyleSheet("background-color: blue")
        self.layout = QGridLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setText(str(0))
        self.display.setAlignment(Qt.AlignRight)

        self.numbers = [QPushButton(str(i)) for i in range(10)]
        self.delete = QPushButton("&C")
        self.multiply = QPushButton("X")
        self.enter = QPushButton("Enter")
        self.enter.setObjectName("Enter")
        self.dot = QPushButton(".")
        self.minus = QPushButton("-")

        #Layout
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

        self.setLayout(self.layout)
