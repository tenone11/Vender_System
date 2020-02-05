# -*- coding: utf-8 -*-

# from PyQt5.QtCore import QUrl
# from PyQt5.QtWebEngineWidgets import QWebEngineView
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


class BrowserWindow(QDialog):
    def __init__(self, _vendor_list, vendor_sum, onevendor_daysum):
        super(BrowserWindow, self).__init__()
        self._vendor_list = _vendor_list
        self.onevendor_sum = vendor_sum
        self.onevendor_daysum = onevendor_daysum
        self.initUI()

    def initUI(self):
        self.setWindowTitle('数据中心')
        self.setGeometry(5, 30, 1920, 1080)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1900, 1000))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
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
        for i in range(len(self._vendor_list)):
            self.groupBox[i] = QtWidgets.QGroupBox(self.tab)
            self.groupBox[i].setGeometry(QtCore.QRect(0, 90 * (i + 1), 500, 80))
            self.groupBox[i].setTitle(self._vendor_list[i])
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

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 357, 41))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.label)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.label_11)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setCurrentIndex(0)

        self.label_4.setText("总支出：%.2f元" % sum(self.onevendor_sum))
        self.label_5.setText("总人天：%.1f" % sum(self.onevendor_daysum))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "常规数据")
        self.label_3.setText("柱状图：")
        self.label_2.setText("X轴：")
        self.label_10.setText("显示选择01")
        self.label.setText("Y轴：")
        self.label_11.setText("显示选择02")
        self.pushButton.setText("OK")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "图表数据分析")


