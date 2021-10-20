#!/usr/bin/env python3
# -*- coding: utf-8 -*


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyQWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        topButton = QPushButton("Top")
        bottomButton = QPushButton("Bottom")

        layout = QVBoxLayout()
        layout.addWidget(topButton)
        layout.addWidget(bottomButton)
        self.setLayout(layout)

        #self.setGeometry(300, 300, 350, 200)
        #self.setWindowTitle("QVBoxLayout")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mqw = MyQWidget()
    sys.exit(app.exec_())

