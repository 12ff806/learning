#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton


class MyQWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        button = QPushButton("Click", self)
        button.clicked.connect(self.on_button_clicked)

        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle("Signals and Slots")
        self.show()
        
    def on_button_clicked(self):
        alert = QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()


class MyButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.initUI()

    def initUI(self):
        self.clicked.connect(self.on_button_clicked)
        self.show()

    def on_button_clicked(self):
        alert = QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #mqw = MyQWidget()

    button = MyButton("Click")

    sys.exit(app.exec_())

