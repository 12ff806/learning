#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)
        
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(10, 150)
        
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle("QComboBox")
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

