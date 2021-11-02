#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QListView
from PyQt5.QtCore import QStringListModel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = QStringListModel([
        "An element",
        "Another element",
        "Yay! Another one."
    ])
    view = QListView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec_())

