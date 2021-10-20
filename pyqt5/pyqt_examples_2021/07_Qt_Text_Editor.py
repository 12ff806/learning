#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtGui import QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI():
        pass
    
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        
        answer = QMessageBox.question(
            window, None, 
            "You have unsaved changes. Save before closing?",
            QMssageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        
        if answer & QMessageBox.Save:
            save()
            if text.document().isModified():
                event.ignore()

        elif answer & QMessageBox.Cancel:
            e.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Text Editor")
    mw = MainWindow()
    sys.exit(app.exec_())

