#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Admin import Login
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class MyWindow(QMainWindow, ):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QDialog()
    ui = Login.LogIn()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

