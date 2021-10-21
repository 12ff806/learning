#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QPlainTextEdit, QMessageBox, QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.filePath = None

        self.initUI()

    def initUI(self):
        # text edit area
        self.text = QPlainTextEdit()
        self.setCentralWidget(self.text)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        # file menu
        openAction = QAction("&Open", self)
        openAction.triggered.connect(self.openFile)
        openAction.setShortcut(QKeySequence.Open)

        saveAction = QAction("&Save", self)
        saveAction.triggered.connect(self.save)
        saveAction.setShortcut(QKeySequence.Save)

        saveAsAction = QAction("Save &As...", self)
        saveAsAction.triggered.connect(self.saveAs)

        closeAction = QAction("&Close", self)
        closeAction.triggered.connect(self.close)
        

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(closeAction)

        # help menu
        aboutAction = QAction("&About", self)
        aboutAction.triggered.connect(self.showAboutDialog)
        
        helpMenu = menubar.addMenu("&Help")
        helpMenu.addAction(aboutAction)

        # show ui
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Text Editor")
        self.show()

    def openFile(self):
        """ open file
        """
        path = QFileDialog.getOpenFileName(self, "Open")[0]
        if path:
            self.text.setPlainText(open(path).read())
            self.filePath = path

    def save(self):
        """ save file
        """
        if self.filePath is None:
            self.saveAs()
        else:
            with open(self.filePath, "w") as f:
                f.write(self.text.toPlainText())
            self.text.document().setModified(False)

    def saveAs(self):
        """ save as
        """
        path = QFileDialog.getSaveFileName(self, "Save As")[0]
        if path:
            self.filePath = path
            self.save()

    def close(self):
        """ close app
        """
        super().close()

    def showAboutDialog(self):
        """ show about dialog
        """
        text = "<center>" \
               "<h1>Text Editor</h1>" \
               "&#8291;" \
               "<img src=icon.svg>" \
               "</center>" \
               "<p>Version 31.4.159.265358<br/>" \
               "Copyright &copy; Company Inc.</p>"
        QMessageBox.about(self, "About Text Editor", text)
    
    def closeEvent(self, e):
        if not self.text.document().isModified():
            return
        
        answer = QMessageBox.question(
            self, None, 
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        
        if answer & QMessageBox.Save:
            self.save()
            if self.text.document().isModified():
                e.ignore()

        elif answer & QMessageBox.Cancel:
            e.ignore()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Text Editor")
    app.setStyle("Fusion")
    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    mw = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

