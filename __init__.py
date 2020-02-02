#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Admin.Login import LogIn
from Main import Main_Window
import sys
from Admin.Sources import user_json
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
# import qdarkstyle
ui = LogIn()


def goto_list():
    accounts = user_json.accounts()
    passwords = user_json.passwords()
    msg = QMessageBox()
    for i in range(len(accounts)):
        if ui.comboBox.currentText() == accounts[i]:
            if ui.textEdit_2.toPlainText() == passwords[i]:
                msg.question(msg, '提示', '登录成功', msg.Ok)
                print("登录成功")
                mainwindow.show()
                dialogWindow.close()
                return 1
            else:
                msg.warning(msg, '提示', '密码错误，请联系雷副部长', msg.Ok)
                print("密码错误，请联系副部长")
                return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogWindow = QDialog()
    mainwindow = QMainWindow()
    ui.setupUi(dialogWindow)
    main_win = Main_Window.Ui_MainWindow()
    main_win.setupUi(mainwindow)
    dialogWindow.show()
    ui.buttonBox.accepted.connect(goto_list)
    main_win.actionExit.triggered.connect(mainwindow.close)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())
