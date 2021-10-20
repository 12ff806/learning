#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class MyQWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #print(dir(self))
        label = QLabel("Hello World!", self)
        #self.addLabel(label)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("QLabel")
        self.show()


class MyQLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        
        self.initUI()

    def initUI(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #ex = MyQWidget()
    
    #mql = MyQLabel("Hello World")
    
    mql = QLabel("Hello World")
    mql.show()

    sys.exit(app.exec_())


