#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from os.path import expanduser
from PyQt5.QtWidgets import QApplication, QDirModel, QTreeView


def main():
    app = QApplication(sys.argv)
    model = QDirModel()
    view = QTreeView()
    view.setModel(model)
    home_directory = expanduser("~")
    view.setRootIndex(model.index(home_directory))
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

