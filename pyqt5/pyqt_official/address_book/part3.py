#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel, QLineEdit, 
        QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget)


class SortedDict(dict):
    class Iterator(object):
        def __init__(self, sorted_dict):
            self._dict = sorted_dict
            self._keys = sorted(self._dict.keys())
            self._nr_items = len(self._keys)
            self._idx = 0

        def __iter__(self):
            return self
        
        def next(self):
            if self._idx >= self._nr_items:
                raise StopIteration

            key = self._keys[self._idx]
            value = self._dict[key]
            self._idx += 1
            
            return key, value
        
        __next__ = next
        
    def __iter__(self):
        return SortedDict.Iterator(self)
    
    iterkeys = __iter__


class AddressBook(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.contacts = SortedDict()
        self.oldName = ""
        self.oldAddress = ""

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.nameLine.setReadOnly(True)

        addressLabel = QLabel("Address:")
        self.addressText = QTextEdit()
        self.addressText.setReadOnly(True)

        self.addButton = QPushButton("&Add")
        self.addButton.show()
        self.submitButton = QPushButton("&Submit")
        self.submitButton.hide()
        self.cancelButton = QPushButton("&Cancel")
        self.cancelButton.hide()
        self.nextButton = QPushButton("&Next")
        self.nextButton.setEnabled(False)
