#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket


def fetch(url):
    sock = socket.socket()
    sock.connect(("number92.tk", 80))
    request = "GET {} HTTP/1.0\r\nHost: number92.tk\r\n\r\n".format(url)
    sock.send(request.encode("utf-8"))
    response = b""
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    print(response)


if __name__ == "__main__":
    fetch("/")

