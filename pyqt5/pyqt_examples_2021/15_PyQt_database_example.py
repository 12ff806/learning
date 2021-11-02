#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
import sys
import os
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


def initdb():
    connection = sqlite3.connect("projects.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE projects
        (url TEXT, descr TEXT, income INTEGER)
    """)
    cursor.execute("""INSERT INTO projects VALUES
        ('giraffes.io', 'Uber, but with giraffes', 1900),
        ('dronesweaters.com', 'Clothes for cold drones', 3000),
        ('hummingpro.io', 'Online humming courses', 120000)
    """)
    connection.commit()


def run():
    if not os.path.exists("projects.db"):
        #print("File projects.db does not exist. Please run initdb.py.")
        #sys.exit()
        
        initdb()

    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("projects.db")
    db.open()
    model = QSqlTableModel(None, db)
    model.setTable("projects")
    model.select()
    view = QTableView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    run()

