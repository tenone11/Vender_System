#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Admin import Login
from Main import Main_Window
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class MyWindow(QMainWindow, ):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogWindow = QDialog()
    mainwindow = QMainWindow()

    ui = Login.LogIn()
    ui.setupUi(dialogWindow)
    main_win = Main_Window.Ui_MainWindow()
    main_win.setupUi(mainwindow)


    def gotoandclose():  # switch page and close dialog
        mainwindow.show()
        dialogWindow.close()


    ui.buttonBox.accepted.connect(gotoandclose)

    dialogWindow.show()
    sys.exit(app.exec_())
