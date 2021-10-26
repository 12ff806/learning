#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit, QAction
from PyQt5.QtGui import QPixmap, QPainter, QKeySequence
from PyQt5.QtCore import QPoint
from PyQt5.QtMultimedia import QSound


class PlainTextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        
        self._holes = []
        self._bullet = QPixmap("bullet.png")
        size = self._bullet.size()
        self._offset = QPoint(size.width() / 2, size.height() / 2)
        
    def mousePressEvent(self, e):
        self._holes.append(e.pos())
        super().mousePressEvent(e)
        self.viewport().update()
        QSound.play("shot.wav")

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self.viewport())
        for hole in self._holes:
            painter.drawPixmap(hole - self._offset, self._bullet)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.filePath = None
        
        self.initUI()

    def initUI(self):
        self.text = PlainTextEdit()
        self.text.setPlainText("Click with the mouse below to shoot ;-)")
        self.setCentralWidget(self.text)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        openAct = QAction("&Open", self)
        openAct.setShortcut(QKeySequence.Open)
        openAct.triggered.connect(self.openFile)

        saveAct = QAction("&Save", self)
        saveAct.triggered.connect(self.save)

        saveAsAct = QAction("Save &As...", self)
        saveAsAct.triggered.connect(self.saveAs)

        closeAct = QAction("&Close", self)
        closeAct.triggered.connect(self.close)
        
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addAction(closeAct)
        
        aboutAct = QAction("&About", self)
        aboutAct.triggered.connect(self.showAboutDialog)
        
        helpMenu = menubar.addMenu("&Help")
        helpMenu.addAction(aboutAct)

        self.show()
        
    def closeEvent(self, e):
        if not self.text.document().isModified():
            return
        
        answer = QMessageBox.question(
            self, None, "You have unsaved changes, Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            self.save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

    def save(self):
        if self.filePath is None:
            self.saveAs()
        else:
            with open(self.filePath, "w") as f:
                f.write(self.text.toPlainText())
            self.text.document().setModified(False)

    def saveAs(self):
        path = QFileDialog.getSaveFileName(self, "Save As")[0]
        if path:
            self.filePath = path
            self.save()
   
    def openFile(self):
        path = QFileDialog.getOpenFileName(self, "Open")[0]
        if path:
            self.text.setPlainText(open(path).read())
            self.filePath = path

    def showAboutDialog(self):
        text = "<center>" \
               "<h1>Text Editor</h1>" \
               "&#8291;" \
               "<img src=icon.svg>" \
               "/center" \
               "<p>Version 31.4.159.265358<br/>" \
               "Copyright &copy; Company Inc.</p>"
        QMessageBox.about(self, "About Text Editor", text)


def run():
    app = QApplication(sys.argv)
    app.setApplicationName("Text Editor")
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()

        
