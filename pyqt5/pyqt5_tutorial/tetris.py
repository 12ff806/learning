#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        """ initiates application UI
        """
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)
        
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        self.tboard.start()
        
        self.resize(180, 380)
        self.center()
        self.setWindowTitle("Tetris")
        self.show()

    def center(self):
        """ centers the window on the screen
        """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))


class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        """ initiates board
        """
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
    
    def shapeAt(self, x, y):
        """ determines shape at the board position
        """
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        """ sets a shape at the board
        """
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        """ returns the width of one square
        """
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """ returns the height of one square
        """
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        """ starts game
        """
        if self.isPaused:
            return
        
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        
        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self):
        """ pauses game
        """
        if not self.isStarted:
            return
        
        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.time.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

    def paintEvent(self, event):
        """ paints all shapes of the game
        """
        painter = QPainter(self)
        rect = self.contentRect()
        

