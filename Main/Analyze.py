# -*- coding: utf-8 -*-
"""
柱状图：
    Y轴 公司 付款金额
    X轴 项目

    Y轴 付款金额
    X轴 项目

    Y轴 公司 付款金额
    X轴 时间 年， 年月， 季度

    Y轴 项目 付款金额
    X轴 时间 年， 年月， 季度

饼状图：
"""

# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QDialog
#
#
# class BrowserWindow(QDialog):
#     def __init__(self, comboBoxList, url):
#         super(BrowserWindow, self).__init__()
#         self.initUI()
#         self.url = url
#         self.comboBoxList = comboBoxList
#
#     def initUI(self):
#         self.setWindowTitle('数据中心')  # 窗口标题
#         self.setGeometry(5, 30, 1355, 730)  # 窗口的大小和位置设置
#
#         self.buttonBox = QtWidgets.QPushButton(self)
#         self.buttonBox.resize(32, 32)
#         self.buttonBox.setText('')
#         self.buttonBox.move(1000, 650)
#         self.comboBox = QtWidgets.QComboBox(self)
#         self.comboBox.addItems(self.comboBoxList)
#         self.browser = QWebEngineView(self)
#         self.browser.resize(900, 600)
#         self.buttonBox.clicked.connect(self.show_chart)
#         # self.browser.setWindowTitle('分析%s' % 'aaa')
#         # 加载html代码(这里注意html代码是用三个单引号包围起来的)
#         # url_string = "file:///C:/Users/Administrator/PycharmProjects/Vender_System/Main/render.html"
#         self.url_string = self.url
#
#         # self.setCentralWidget(self.browser)
#     def show_chart(self):
#         self.browser.load(QUrl(self.url_string))

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pandas as pd
from Main.Features import Features
import os

class BrowserWindow(QDialog):
    def __init__(self, vendor_dict, vendor_list):
        super(BrowserWindow, self).__init__()
        self.pd_dict = vendor_dict
        self.vendor_list = vendor_list
        self.onevendor_sum = []
        self.onevendor_daysum = []
        self.features = Features(self.pd_dict)
        self.onevendor_daysum = self.features.get_base_sum('总人天')
        self.onevendor_sum = self.features.get_base_sum('付款金额')
        self.initUI()
        self.msg = QtWidgets.QMessageBox()

    def initUI(self):
        self.setWindowTitle('数据中心')
        self.setGeometry(5, 30, 1920, 1080)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1900, 1000))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)

        # Tab1
        self.tab = QtWidgets.QWidget()
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 100, 32))
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 40, 200, 32))
        self.groupBox = {}
        self.label_groupBox = {}
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 631, 441))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.tab)


        for i in range(len(self.vendor_list)):
            self.groupBox[i] = QtWidgets.QGroupBox(self.tab)
            self.groupBox[i].setGeometry(QtCore.QRect(0, 90 * (i + 1), 500, 80))
            self.groupBox[i].setTitle(self.vendor_list[i])
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(10)
            self.groupBox[i].setFont(font)
            self.label_groupBox[i] = QtWidgets.QLabel(self.groupBox[i])
            self.label_groupBox[i].setText('总支出：%.2f元' % self.onevendor_sum[i])
            self.label_groupBox[i].setGeometry(QtCore.QRect(10, 20, 400, 40))
            font.setBold(False)
            font.setPointSize(8)
            self.label_groupBox[i].setFont(font)
            self.label_groupBox[i + 1] = QtWidgets.QLabel(self.groupBox[i])
            self.label_groupBox[i + 1].setText('总人天：%.1f' % self.onevendor_daysum[i])
            self.label_groupBox[i + 1].setGeometry(QtCore.QRect(10, 40, 400, 40))
            self.label_groupBox[i + 1].setFont(font)
        self.label_4.setText("总支出：%.2f元" % sum(self.onevendor_sum))
        self.label_5.setText("总人天：%.1f" % sum(self.onevendor_daysum))

        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "常规数据")
        # Tab2
        self.tab_2 = QtWidgets.QWidget()
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1000, 41))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_01 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.comboBox_01)
        self.comboBox_01_02 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.comboBox_01_02)
        self.pushButton_insert = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.pushButton_insert)
        self.pushButton_insert.setText("插入")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox_02 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.comboBox_02)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setCurrentIndex(0)
        self.label_3.setText("柱状图：")
        self.label_2.setText("Y轴：")
        self.label.setText("X轴：")
        self.pushButton.setText("OK")
        self.browser = QWebEngineView(self.tab_2)
        self.browser.setGeometry(QtCore.QRect(0, 50, 800, 600))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "图表数据分析")

        self.comboBox_01.addItems(self.vendor_list)
        item1 = ['付款金额', '不含税金额', '总人天']
        item2 = ['游戏项目', '类型', '项目部门']
        self.comboBox_01_02.addItems(item1)
        self.comboBox_02.addItems(item2)

        self.pushButton_insert.clicked.connect(self.get_barlist)
        self.pushButton.clicked.connect(self.show_bar)
    # comboBox_01 公司名称   comboBox_01_02 钱    comboBox_02 项目
    def get_barlist(self):
        self.y_list = []
        self.vendor_name = self.comboBox_01.currentText()
        self.project_name = self.comboBox_02.currentText()
        self.result = self.comboBox_01_02.currentText()
        self.get_res = self.features.get_project_sum(self.vendor_name, self.project_name, self.result)
        self.y_list.append([self.get_res[0], self.get_res[2]])
        self.msg.information(self.msg, '提示', '添加成功', self.msg.Ok)

    def show_bar(self):
        self.x_list = self.get_res[1]
        print(self.x_list)
        print(self.y_list)
        self.features.create_bar(self.x_list, self.y_list)
        root_path = os.path.abspath(os.path.dirname(__file__))
        url_string = "file:///C:/Users/Administrator/PycharmProjects/Vender_System/Main/Source/bar.html"
        self.browser.load(QUrl(url_string))
    #
    #     print(x_list)

    #     url_string = "file:///C:/Users/Administrator/PycharmProjects/Vender_System/Main/render.html"
    #     self.browser.load(QUrl(url_string))
        # sum_list = []
        # manday_list = []
        # vendor_dict = self.get_vendor_info()
        # features = Features.Features()
        # for i in vendor_dict:
        #     _sum = features.get_sum(vendor_dict[i]['付款金额'])
        #     _manday = features.get_sum(vendor_dict[i]['总人天'])
        #     sum_list.append(_sum)
        #     manday_list.append(_manday)
        # a = Analyze.BrowserWindow(self.vendor_list, sum_list, manday_list)
