#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load("main.qml")
    sys.exit(app.exec_())


