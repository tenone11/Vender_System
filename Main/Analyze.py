# -*- coding: utf-8 -*-

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog


class BrowserWindow(QDialog):
    def __init__(self, comboBoxList, url):
        super(BrowserWindow, self).__init__()
        self.initUI()
        self.url = url
        self.comboBoxList = comboBoxList

    def initUI(self):
        self.setWindowTitle('数据中心')  # 窗口标题
        self.setGeometry(5, 30, 1355, 730)  # 窗口的大小和位置设置

        self.buttonBox = QtWidgets.QPushButton(self)
        self.buttonBox.resize(32, 32)
        self.buttonBox.setText('')
        self.buttonBox.move(1000, 650)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItems(self.comboBoxList)
        self.browser = QWebEngineView(self)
        self.browser.resize(900, 600)
        self.buttonBox.clicked.connect(self.show_chart)
        # self.browser.setWindowTitle('分析%s' % 'aaa')
        # 加载html代码(这里注意html代码是用三个单引号包围起来的)
        # url_string = "file:///C:/Users/Administrator/PycharmProjects/Vender_System/Main/render.html"
        self.url_string = self.url

        # self.setCentralWidget(self.browser)
    def show_chart(self):
        self.browser.load(QUrl(self.url_string))



