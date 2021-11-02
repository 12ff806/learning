#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant


headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]


class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)
    def columnCount(self, parent):
        return len(headers)
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return headers[section]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = TableModel()
    view = QTableView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec_())

