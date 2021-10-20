#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType("dialog.ui")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    sys.exit(app.exec_())

