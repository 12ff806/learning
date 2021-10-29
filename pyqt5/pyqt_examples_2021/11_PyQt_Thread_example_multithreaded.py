#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from requests import Session
from threading import Thread
from time import sleep
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QLineEdit, QWidget, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.textArea = QPlainTextEdit()
        self.textArea.setFocusPolicy(Qt.NoFocus)
        
        self.message = QLineEdit()
        self.message.returnPressed.connect(self.sendMessage)
        
        layout = QVBoxLayout()
        layout.addWidget(self.textArea)
        layout.addWidget(self.message)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayNewMessage)
        self.timer.start(1000)

        self.setLayout(layout)
        self.show()

    def sendMessage(self):
        server.post(chatUrl, {"name": name, "message": self.message.text()})
        self.message.clear()

    def displayNewMessage(self):
        #newMessage = server.get(chatUrl).text
        if newMessage:
            self.textArea.appendPlainText(newMessage.pop(0))


def fetNewMessage():
    while True:
        response = server.get(chatUrl).text
        if response:
            newMessage.append(response)
        sleep(0.5)


def main():
    app = QApplication(sys.argv)
    w = Widget()
    
    thread = Thread(target=fetNewMessage, daemon=True)
    thread.start()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    name = input("Please enter your name: ")
    chatUrl = "https://build-system.fman.io/chat"
    server = Session()
    newMessage = []
    main()

